"""Compatibility constants shared by supported QGIS 3 and QGIS 4 releases.

QGIS moved a number of enums to :class:`Qgis` while preparing for QGIS 4.
The newer names are available in recent QGIS 3 releases too, but Netflora's
minimum supported release (3.22) still needs the original enum locations.
"""

from qgis.core import (
    Qgis,
    QgsProcessing,
    QgsProcessingParameterDefinition,
    QgsProcessingParameterFile,
    QgsProcessingParameterNumber,
    QgsWkbTypes,
)
from qgis.PyQt.QtCore import Qt


try:
    PROCESSING_VECTOR_POINT = Qgis.ProcessingSourceType.VectorPoint
    PROCESSING_VECTOR_LINE = Qgis.ProcessingSourceType.VectorLine
    PROCESSING_VECTOR_POLYGON = Qgis.ProcessingSourceType.VectorPolygon
except AttributeError:  # QGIS < 3.36
    PROCESSING_VECTOR_POINT = QgsProcessing.TypeVectorPoint
    PROCESSING_VECTOR_LINE = QgsProcessing.TypeVectorLine
    PROCESSING_VECTOR_POLYGON = QgsProcessing.TypeVectorPolygon

try:
    PROCESSING_NUMBER_DOUBLE = Qgis.ProcessingNumberParameterType.Double
    PROCESSING_FILE = Qgis.ProcessingFileParameterBehavior.File
    PROCESSING_PARAMETER_HIDDEN = Qgis.ProcessingParameterFlag.Hidden
except AttributeError:  # QGIS < 3.36
    PROCESSING_NUMBER_DOUBLE = QgsProcessingParameterNumber.Double
    PROCESSING_FILE = QgsProcessingParameterFile.File
    PROCESSING_PARAMETER_HIDDEN = QgsProcessingParameterDefinition.FlagHidden


try:
    WKB_POINT = Qgis.WkbType.Point
    WKB_LINE_STRING = Qgis.WkbType.LineString
    WKB_POLYGON = Qgis.WkbType.Polygon
except AttributeError:  # QGIS < 3.30
    WKB_POINT = QgsWkbTypes.Point
    WKB_LINE_STRING = QgsWkbTypes.LineString
    WKB_POLYGON = QgsWkbTypes.Polygon


try:
    BLOCKING_QUEUED_CONNECTION = Qt.ConnectionType.BlockingQueuedConnection
    DASH_LINE = Qt.PenStyle.DashLine
except AttributeError:  # Qt 5
    BLOCKING_QUEUED_CONNECTION = Qt.BlockingQueuedConnection
    DASH_LINE = Qt.DashLine
