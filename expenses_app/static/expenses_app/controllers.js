var expensesApp = angular.module('expensesApp', []).config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});

$(document).ready(function() {
    $(".select-on-focus").focus(function() { $(this).select(); } );
});

expensesApp.directive('replacecomma', function () {
    return {
        require: 'ngModel',
        link: function (scope, element, attrs, ngModelCtrl) {
            scope.$watch(attrs.ngModel, function (newVal) {
                if (newVal !== undefined && newVal !== null) {
                    ngModelCtrl.$setViewValue(String(newVal).replace(/,/g, '.'));
                    element.val(String(newVal).replace(/,/g, '.'));
                }
            })

        }
    }
});

expensesApp.controller('NewBillCtrl', function ($scope) {
    $scope.bill = {
        'sum': 0,
        'billRows': [{'sum': 0, 'label': ''}],
        submit: function(event) {
            var tmpSum = 0;

            for (i = 0; i < $scope.bill.billRows.length; i++) {
                tmpSum = parseFloat(tmpSum) + parseFloat($scope.bill.billRows[i].sum);
            }

            if (Number(tmpSum.toFixed(2)) != $scope.bill.sum) {
                alert('Bill rows sum is invalid!');
                event.preventDefault();
            } else if (!$scope.billForm.$valid) {
                event.preventDefault();
            }
        },
        updateRows: function() {
            var tmpSum = parseFloat($scope.bill.sum);
            var billRowsLength = $scope.bill.billRows.length;

            for (i = 0; i < billRowsLength - 1; i++) { // We do not want to count last element
                tmpSum = parseFloat(tmpSum) - parseFloat($scope.bill.billRows[i].sum);
            }

            $scope.bill.billRows[billRowsLength - 1].sum = parseFloat(tmpSum).toFixed(2).replace('.', ',');
        }
    };

    var sumRegex = /^[\d]+[\.,]?[\d]{0,2}$/;
    $scope.sumPattern = sumRegex;

    $scope.addRow = function() {
        $scope.bill.billRows.push({'sum': 0, 'label': ''});
        $scope.bill.updateRows();
    }

    $scope.deleteRow = function(index) {
        $scope.bill.billRows.splice(index, 1);
    }

    $scope.$watch('bill.sum', function(newValue, oldValue) {
        $scope.bill.updateRows();
    }, true);
});

expensesApp.controller('ChartsCtrl', function ($scope, $http) {
    $http.get(config['url_two_weeks_data'], config).then(function(data, status, headers, config) {
        var chartData = {
            'labels': [],
            'datasets': [
                {
                    label: 'Amount spent each day',
                    fillColor: 'rgba(151,187,205,0.2)',
                    strokeColor: 'rgba(151,187,205,1)',
                    pointColor: 'rgba(151,187,205,1)',
                    pointStrokeColor: '#fff',
                    pointHighlightFill: '#fff',
                    pointHighlightStroke: 'rgba(151,187,205,1)',
                    data: []
                }
            ]
        };

        var keysSorted = Object.keys(data['data']).sort(function(a, b) {
            if (a < b) {
                return -1;
            } else if (a > b) {
                return 1;
            }

            return 0;
        });

        for (var i = 0; i < keysSorted.length; i++) {
            if (data['data'].hasOwnProperty(keysSorted[i])) {
                chartData['labels'].push(keysSorted[i]);
                chartData['datasets'][0]['data'].push(data['data'][keysSorted[i]]);
            }
        }

        var ctx = document.getElementById('billsChart').getContext('2d');
        var myNewChart = new Chart(ctx).Line(chartData);
    });
});