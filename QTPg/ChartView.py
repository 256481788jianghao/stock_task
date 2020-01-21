'''
Created on 2020年1月9日

@author: Administrator
'''
from PyQt5 import QtChart,QtCore

class ChartView(object):
    '''
    classdocs
    '''


    def __init__(self, baseWidget):
        self.chartView = QtChart.QChartView(baseWidget)
        self.chartView.setGeometry(0,0,baseWidget.width(),baseWidget.height())
        self.chartView.setRubberBand(QtChart.QChartView.HorizontalRubberBand)
        self.chartView.rubberBandChanged.connect(self._rubberBandChangedFun)
        #print(baseWidget.width())
    def _rubberBandChangedFun(self,rubberBandRect, fromScenePoint, toScenePoint):
        print(rubberBandRect)
        print(fromScenePoint)
        print(toScenePoint)
        
    def SetXAxis(self,maxValue,step):
        pass
    def SetYAxis(self,maxValue,step):
        pass
    
    def SetLineSeries(self,data_x,data_y,data_y_2=None,chart_name=''):
        self.chart = QtChart.QChart()
        #self.chart.setTheme(QtChart.QChart.ChartThemeDark)
        
        series = QtChart.QLineSeries()
        for index in range(len(data_y)):
            series.append(index, data_y[index])
        self.chart.addSeries(series)
        
        axisX = QtChart.QCategoryAxis()
        axisX.setRange(-1,len(data_y)+1)
        axisX.setStartValue(0)
        for index in range(0,len(data_x)):
            axisX.append(data_x[index],index)
        axisX.setLabelsAngle(90)
        #axisX.setTickCount(10)
        axisX.setLabelsPosition(QtChart.QCategoryAxis.AxisLabelsPositionOnValue)
        #self.chart.setAxisX(axisX,series)
        self.chart.addAxis(axisX,QtCore.Qt.AlignBottom)
        
        series.attachAxis(axisX)
        
        axisY = QtChart.QValueAxis()
        axisY.setRange(data_y.min(),data_y.max())
        axisY.setTickCount(10)
        self.chart.addAxis(axisY,QtCore.Qt.AlignLeft)
        #self.chart.setAxisY(axisY,series)
        series.attachAxis(axisY)
        
        if data_y_2 is not None:
            axisY2 = QtChart.QValueAxis()
            axisY2.setRange(data_y_2.min(),data_y_2.max())
            axisY2.setTickCount(10)
            self.chart.addAxis(axisY2,QtCore.Qt.AlignRight)
            series2 = QtChart.QLineSeries()
            for index in range(len(data_y_2)):
                series2.append(index, data_y_2[index])
            self.chart.addSeries(series2)
            series2.attachAxis(axisX)
            series2.attachAxis(axisY2)
        
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
        