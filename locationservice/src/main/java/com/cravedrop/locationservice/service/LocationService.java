package com.cravedrop.locationservice.service;

import com.cravedrop.locationservice.dto.NearbyRiderResponse;
import com.cravedrop.locationservice.dto.RiderLocationRequest;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.data.geo.*;
import org.springframework.data.redis.connection.RedisGeoCommands;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
@Slf4j
@RequiredArgsConstructor
public class LocationService {

    private final RedisTemplate<String, String> redisTemplate;

    // redis key
    private static final String RIDERS_GEO_KEY = "riders:locations";

    // update rider in redis
    public void updateRiderLocation(RiderLocationRequest riderLocationRequest) {
        log.info("Updating location for rider {}", riderLocationRequest.getRiderId());

        // ⚠️ LONGITUDE 1st in redis
        Point riderPoint = new Point(riderLocationRequest.getLongitude(), riderLocationRequest.getLatitude());

        redisTemplate.opsForGeo().add(RIDERS_GEO_KEY, riderPoint, riderLocationRequest.getRiderId());

        log.info("Location updated for rider: {}", riderLocationRequest.getRiderId());
    }

    public List<NearbyRiderResponse> getNearByRiders(
            double latitude,  double longitude, double radiusInKm) {

        log.info("Finding drivers near lat: {} long: {} within {} km", latitude, longitude, radiusInKm);

        // ⚠️ LONGITUDE 1st in redis
        Circle searchArea = new Circle(
                new Point(longitude, latitude),
                new Distance(radiusInKm, Metrics.KILOMETERS)
        );

        GeoResults<RedisGeoCommands.GeoLocation<String>> results =
                redisTemplate.opsForGeo().radius(
                        RIDERS_GEO_KEY,
                        searchArea,
                        RedisGeoCommands.GeoRadiusCommandArgs.newGeoRadiusArgs()
                                .includeCoordinates()
                                .includeDistance()
                                .sortAscending()
                                .limit(10)
                );

        List<NearbyRiderResponse> nearbyRiders = new ArrayList<>();

        if (results != null){
            results.getContent().forEach(result -> {
                RedisGeoCommands.GeoLocation<String> location = result.getContent();
                nearbyRiders.add(new NearbyRiderResponse(
                        location.getName(),
                        location.getPoint().getY(),
                        location.getPoint().getX(),
                        result.getDistance().getValue()
                ));
            });
        }
        log.info("Found {} drivers nearby", nearbyRiders.size());
        return nearbyRiders;
    }

    // remove rider from redis when go offline
    public void removeRider(String riderId) {
        log.info("Removing driver {}", riderId);
        redisTemplate.opsForGeo().remove(RIDERS_GEO_KEY, riderId);
    }


}
