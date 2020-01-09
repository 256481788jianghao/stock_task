'''
Created on 2020年1月9日

@author: Administrator
'''
from PyQt5 import QtChart

class ChartView(object):
    '''
    classdocs
    '''


    def __init__(self, baseWidget):
        self.chartView = QtChart.QChartView(baseWidget)
        self.chartView.setGeometry(0,0,baseWidget.width(),baseWidget.height())
        #print(baseWidget.width())
        
    def SetXAxis(self,maxValue,step):
        pass
    def SetYAxis(self,maxValue,step):
        pass
    
    def SetLineSeries(self,data_x,data_y,chart_name=''):
        series = QtChart.QLineSeries()
        for index in range(len(data_x)):
            series.append(data_x[index], data_y[index])
        self.chart = QtChart.QChart()
        self.chart.addSeries(series)
        self.chart.setTitle(chart_name)
        self.chart.createDefaultAxes()
        
    def Show(self):
        self.chartView.setChart(self.chart)
        