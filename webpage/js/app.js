angular.module('NNApp', [])
    .controller('NNController', function ($scope, $http) {
        $scope.brailleText = [];
        $scope.translateToBraille = function () {
            $scope.brailleText = [];
            $scope.trained=false;

            console.log($scope.sendText);
            var chars = $scope.sendText.split('');
            console.log(chars);
            chars.forEach(function (e) {
                $scope.brailleText.push({braillePath: "img/" + e + ".PNG"});
            });
            console.log($scope.brailleText);
        };
        $scope.sendParams = function () {
           $scope.trained=false;
            var data = $.param({
                epoch: $scope.epoch,
                hidden: $scope.hiddenLayer,
                learningRate: $scope.learningRate

            });
            var req = {
                method: 'POST',
                url: 'http://localhost:5000/translate',
                headers: {
                    'Content-Type': undefined
                },
                data: data
            }
            $http(req).then(function () {
                console.log("success Param");
                $scope.trained = true;
            }, function () {
                console.log("failed PAram");
            });

        };
        $scope.sendToNetwork = function () {
            var req = {
                method: 'POST',
                url: 'http://localhost:5000/translate',
                headers: {
                    'Content-Type': undefined
                },
                data: {text: $scope.sendText}
            }
            $http(req).then(function (data) {
                console.log(data);
                $scope.result = data
            }, function () {
                console.log("failed")
            });

        };

    });