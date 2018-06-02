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
           
            var req = {
                method: 'POST',
                url: 'http://localhost:5000/train',
                headers: {
                    'Content-Type': "application/json"
                },
                data: {
					epoch: $scope.epoch,
					hiddenLayer: $scope.hiddenLayer,
					learningRate: $scope.learningRate
					}
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
                    'Content-Type': "application/json"
                },
                data: {text: $scope.sendText}
            }
            $http(req).then(function (response) {
                console.log(response);
                $scope.result = response.data
            }, function () {
                console.log("failed")
            });

        };

    });