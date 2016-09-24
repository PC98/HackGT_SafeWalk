//
//  Point.swift
//  RPrepSearch
//
//  Created by Nidhi on 9/24/16.
//  Copyright © 2016 Nidhi. All rights reserved.
//

import UIKit

class Point: NSObject {
    var lattitude = 33.772463
    var longitude = -84.391272
    var crimes = 0;
    
    
    init(longitude: Double,
        lattitude: Double,
        crimes: Int
        
        )
    {
        self.longitude = longitude
        self.lattitude = lattitude
        self.crimes = crimes
        
        
    }
    
    
}
