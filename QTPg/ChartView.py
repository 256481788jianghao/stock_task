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
        self.chart = QtChart.QChart()
        axisX = QtChart.QCategoryAxis()
        axisX.setRange(-1,len(data_y)+1)
        axisX.setStartValue(0)
        for index in range(len(data_x)):
            axisX.append(data_x[index],index)
        axisX.setLabelsAngle(90)
        series = QtChart.QLineSeries()
        for index in range(len(data_y)):
            series.append(index, data_y[index])
        self.chart.addSeries(series)
        axisX.setLabelsPosition(QtChart.QCategoryAxis.AxisLabelsPositionOnValue)
        self.chart.setAxisX(axisX,series)
        self.chart.setTitle(chart_name)
        
    def SetLineSeriesData(self,data_list,chart_name=''):
        self.chart = QtChart.QChart()
        for data_lines in data_list:
            series = QtChart.QLineSeries()
            for index in range(len(data_lines)):
                series.append(index, data_lines[index])
            self.chart.addSeries(series)
        self.chart.setTitle(chart_name)
        self.chart.createDefaultAxes()
        
    def Show(self):
        self.chartView.setChart(self.chart)
        