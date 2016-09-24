//
//  PointFactory.swift
//  RPrepSearch
//
//  Created by Nidhi on 9/24/16.
//  Copyright © 2016 Nidhi. All rights reserved.
//

import UIKit

class PointFactory: NSObject {
    
    private var resultDictionary = NSMutableDictionary();
    private var listOfPoints = NSMutableArray();
    
    private func loadPointData()
    {
        let paths = NSSearchPathForDirectoriesInDomains(.DocumentDirectory, .UserDomainMask, true) as NSArray
        
        let documentsDirectory = paths[0] as! String
        
        let doc = NSURL(string: documentsDirectory)
        let path = doc!.URLByAppendingPathComponent("PointData.plist")
        
        let stringPath = "\(path)" //this is the file path as a string
        
        
        //get the file manager to work with our file
        let fileManager = NSFileManager.defaultManager()
        
        
        
        //check if file exists
        if(!fileManager.fileExistsAtPath(stringPath))
        {
            // If it doesn't, copy it from the default file in the Bundle
            if let bundlePath = NSBundle.mainBundle().pathForResource("PointData", ofType: "plist")
            {
                self.resultDictionary = NSMutableDictionary(contentsOfFile: bundlePath)!
                print(self.resultDictionary)
                //fileManager.copyItemAtPath(bundlePath, toPath: path)
                
            }
            else
            {
                print("PointData.plist not found. Please, make sure it is part of the bundle.")
            }
        }
        else
        {
            print("PointData.plist already exits at path.")
            // use this to delete file from documents directory
            //fileManager.removeItemAtPath(path, error: nil)
        }

    }
    
    
    
    
}
