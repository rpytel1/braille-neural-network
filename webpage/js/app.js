angular.module('NNApp', [])
    .controller('NNController', ['$scope','$http' ,function ($scope,$http) {
        $scope.brailleText = [];
        $scope.translateToBraille = function () {
            $scope.brailleText = [];
            console.log($scope.sendText);
            var chars = $scope.sendText.split('');
            console.log(chars);
            chars.forEach(function (e) {
                $scope.brailleText.push({braillePath: "img/" + e + ".PNG"});
            });
            console.log($scope.brailleText);
        };

        $scope.sendToNetwork = function () {
            $http.post("http://localhost:8080/network", {
                'text': $scope.sendText,
                'epoch':$scope.epoch,
                'learningRate':$scope.learningRate,
                'hiddenLayer': $scope.hiddenLayer
            })
                .success(function (response) {
                    console.log(response.data);
                    $scope.result = response.data;
                });
        };

    }]);