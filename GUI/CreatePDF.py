from reportlab.graphics.charts.axes import XValueAxis
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.barcharts import VerticalBarChart
from database.CSC100DB import CSC100DB


class CreatePDF:

    def __init__(self):
        self.db = CSC100DB()

    def getKeys(self, dictionary):
        return list(dictionary.keys())

    def getValues(self, dictionary):
        return list(dictionary.values())

    def getDB(self):
        return self.db

    def drawBarChart(self, xValues, yValues):
        drawing = Drawing(400, 200)

        yValues = [tuple(yValues)]

        bc = VerticalBarChart()
        bc.x = 50
        bc.y = 50
        bc.height = 125
        bc.width = 300
        bc.data = yValues
        bc.strokeColor = colors.black

        bc.valueAxis.valueMin = 0
        bc.valueAxis.valueMax = 250
        bc.valueAxis.valueStep = 25

        bc.categoryAxis.labels.boxAnchor = 'ne'
        bc.categoryAxis.labels.dx = 8
        bc.categoryAxis.labels.dy = -2
        bc.categoryAxis.labels.angle = 45
        bc.categoryAxis.categoryNames = xValues

        drawing.add(bc)

        renderPDF.drawToFile(drawing, 'reports/test.pdf', 'My First Drawing')

    def drawLGABarChart(self):
        dictionary = self.getDB().getMonthlyDataForLGA('01', 2018)
        xValues = self.getKeys(dictionary)
        yValues = self.getValues(dictionary)
        self.drawBarChart(xValues, yValues)

    def drawTaxonsBarChart(self):
        dictionary = self.getDB().getMonthlyDataForTaxons('01', 2018)
        xValues = self.getKeys(dictionary)
        yValues = self.getValues(dictionary)
        self.drawBarChart(xValues, yValues)


pdf = CreatePDF()

print(pdf.getKeys(pdf.getDB().getMonthlyDataForTaxons('01', 2018)))
print(pdf.getValues(pdf.getDB().getMonthlyDataForTaxons('01', 2018)))
pdf.drawTaxonsBarChart()
