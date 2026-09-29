package com.cravedrop.locationservice.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class RiderLocationRequest {
    private String riderId;
    private Double latitude;
    private Double longitude;


}
