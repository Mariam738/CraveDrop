package com.cravedrop.locationservice.controller;

import com.cravedrop.locationservice.dto.NearbyRiderResponse;
import com.cravedrop.locationservice.dto.RiderLocationRequest;
import com.cravedrop.locationservice.service.LocationService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/v1/locations")
@Slf4j
@RequiredArgsConstructor
public class LocationController {
    private final LocationService locationService;

    // Rider's phone calls this every 3 seconds
    @PostMapping("/riders/update")
    public ResponseEntity<String> updateRiderLocation (
            @RequestBody RiderLocationRequest riderLocationRequest
            )  {
        locationService.updateRiderLocation(riderLocationRequest);
        return ResponseEntity.ok("Rider Location updated");
    }

    @GetMapping("/riders/nearby")
    public ResponseEntity<List<NearbyRiderResponse>> getNearbyDrivers (
            @RequestParam double latitude,
            @RequestParam double longitude,
            @RequestParam (defaultValue = "5.0") double radius
    )  {
        return ResponseEntity.ok(locationService.getNearByRiders(latitude, longitude, radius));
    }

    @DeleteMapping("/riders/{riderId}")
    public ResponseEntity<String> removeRider (
            @PathVariable String riderId
    )  {
        locationService.removeRider(riderId);
        return ResponseEntity.ok("Rider removed successfully");
    }


}

