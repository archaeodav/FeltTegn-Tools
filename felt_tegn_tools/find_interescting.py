# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:31:19 2022

@author: au526889
"""

import os

import json

from qgis import processing

from qgis.processing import alg

from qgis.core import (QgsProject,
                       QgsVectorLayer)



class FindIntersections():
    def __init__(self,
                 polys : QgsVectorLayer):
        
        self.polys = polys
        
        self.intersecting = self.get_intersecting()
        
        
    def get_intersecting(self):
        
        intersecting = []
        
        features = self.polys.getFeatures()
        
        for f1 in features:
            f1_id = f1.id()
            f1_geom = f1.geometry()
            f1_area = f1_geom.area
            
            for f2 in features:
                intersection = None
                f2_id = f2.id()
                
                if not f2_id == f1_id:
                    f2_geom = f2.geometry()
                    
                    if f1_geom.intersects(f2_geom):
                        f2_area = f2_geom.area()
                        
                        if f1_area < f2_area:
                            intersection = (f1_id,
                                            f2_id,
                                            f1_geom.boundingBox(),
                                            f1_geom.area())
                        else:
                            intersection = (f2_id,
                                            f1_id,
                                            f2_geom.boundingBox(),
                                            f2_geom.area())
                            
                if not intersection is None:
                    if not intersection in intersecting:
                        intersecting.append(intersection)
        
        return intersecting
    
    def get_intersection(self,
                         idx):
        
        return self.intersecting
    
    def get_multiple(self):
        multiples = {}
        
        for row in self.intersecting:
            if not row[1] in multiples.keys():
                multiples[row[1]]=[(row[0],row[2]),row[3]]
                
            else:
                multiples[row[1]].append((row[0],row[2],row[3]))
                
        return multiples
    
    
            
    