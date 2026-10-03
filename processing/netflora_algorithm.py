from qgis.core import (
    QgsProcessingAlgorithm, QgsProcessingParameterRasterLayer, QgsProcessingParameterFeatureSink,
    QgsProcessingParameterNumber, QgsProcessingOutputVectorLayer, QgsProcessingContext,
    QgsProcessingFeedback, QgsVectorLayer, QgsFields, QgsField, QgsFeature,
    QgsFeatureSink, QgsPointXY, QgsGeometry
)
from qgis.PyQt.QtCore import QVariant

from ..common.qgis_compat import PROCESSING_VECTOR_POINT, WKB_POINT

class NetfloraDetector(QgsProcessingAlgorithm):
    INPUT_RASTER = 'INPUT_RASTER'
    CONFIDENCE = 'CONFIDENCE'
    OUTPUT = 'OUTPUT'

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterRasterLayer(self.INPUT_RASTER, "Imagem de entrada"))
        self.addParameter(QgsProcessingParameterNumber(self.CONFIDENCE, "Confiança mínima", defaultValue=0.25))
        self.addParameter(QgsProcessingParameterFeatureSink(self.OUTPUT, "Saída das detecções", type=PROCESSING_VECTOR_POINT))

    def processAlgorithm(self, parameters, context: QgsProcessingContext, feedback: QgsProcessingFeedback):
        raster_layer = self.parameterAsRasterLayer(parameters, self.INPUT_RASTER, context)
        confidence = self.parameterAsDouble(parameters, self.CONFIDENCE, context)

        results = [(raster_layer.extent().center().x(), raster_layer.extent().center().y())]  # dummy

        (sink, dest_id) = self.parameterAsSink(
            parameters,
            self.OUTPUT,
            context,
            QgsFields([QgsField('id', QVariant.Int)]),
            WKB_POINT,
            raster_layer.crs()
        )

        for i, (x, y) in enumerate(results):
            feat = QgsFeature()
            feat.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(x, y)))
            feat.setAttributes([i])
            sink.addFeature(feat, QgsFeatureSink.FastInsert)

        return {self.OUTPUT: dest_id}

    def name(self):
        return 'netflora_detector'

    def displayName(self):
        return 'Detecção de Palmeiras (NetFlora)'

    def group(self):
        return 'NetFlora'

    def groupId(self):
        return 'netflora'

    def createInstance(self):
        return NetfloraDetector()
