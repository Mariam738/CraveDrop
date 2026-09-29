package com.cravedrop.locationservice.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class NearbyRiderResponse {
    private String RiderId;
    private Double latitude;
    private Double longitude;
    private Double distanceInKm;

}
