var expensesApp = angular.module('expensesApp', []).config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});

expensesApp.controller('NewBillCtrl', function ($scope) {
    $scope.billRows = [{}];

    $scope.addRow = function() {
        $scope.billRows.push({});
    }

    $scope.deleteRow = function(index) {
        $scope.billRows.splice(index, 1);
    }
});