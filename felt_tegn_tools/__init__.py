# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FeltTegnTools
                                 A QGIS plugin
 Plugin for postprocessing survey data
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-05-23
        copyright            : (C) 2022 by David Stott /  Moesgaard Museum
        email                : ds@moesgaardmuseum.dk
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load FeltTegnTools class from file FeltTegnTools.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .felt_tegn_tools import FeltTegnTools
    return FeltTegnTools(iface)
