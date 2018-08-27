(function(){
    'use strict';
    var app = angular.module('isamm.demo', ['ngCookies']).config(function($httpProvider) {
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
        });




    app.controller('IsammController', ['$scope', '$http' ,function ($scope,$http) {

 





            $scope.data = [];
            
        
                $http.get('/isamm/activity').then(function(response){
                    $scope.data = response.data;
            
                });
            }]);
    

            app.controller('DemandeController', function ($scope,$http) {
            $scope.demandes = [];
            
            $http.get('/isamm/demandes/').then(function(response){
                $scope.demandes = response.data;
        
            });

            

            
    
            
            });

            app.controller('EventsController', function ($scope,$http) {
            $scope.events = [];
           
                
            $http.get('/isamm/events').then(function(response){
                $scope.events = response.data;
           
            });
            });


      
             
           

                app.controller('CalenderController', function($scope, $http) {
                    $scope.submit = function() {
                    var in_data = { 'subject': '$scope.subject '};
                    $http.post('/isamm/event/summer_school_2/', in_data)
                    .success(function(out_data) {
                    alert("yes");
                    });
                    }
                    });
                    


    
 
}());