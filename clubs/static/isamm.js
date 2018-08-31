(function(){
    'use strict';
    var app = angular.module('isamm.demo', ['ngCookies']).config(function($httpProvider) {
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
        });

        app.controller('usercontroller', ['$scope', '$http' ,function ($scope,$http) {
           
            $http.get('/isamm/profiles/').then(function(response){
                $scope.countryList = []; 
                var users =[]
                users = response.data;
                
                  
                   
                    
                   
                    var v;
                    for (v = 1; v<  users.length; v++) {
                        
                        $scope.countryList.push(users[v].username)
                    }
                  
    
            
            
           
                    $scope.hidesrch = true;  

           $scope.complete = function(string){  
                $scope.hidethis = false;  
                
                var output = [];  
                angular.forEach($scope.countryList, function(country){  
                     if(country.toLowerCase().indexOf(string.toLowerCase()) >= 0)  
                     {  
                          output.push(country);  
                     }  
                });  
                $scope.filterCountry = output;  
           }  
           
           $scope.fillTextbox = function(string){  
                $scope.country = string;  
                $scope.hidesrch = false;  
                $scope.hidethis = true; 

                
                for (v = 1; v<  users.length; v++) {
                        
                   if( users[v].username==string)
                    {
                        $scope.pic = users[v].image
                        $scope.firstname = users[v].first_name
                        $scope.lastname = users[v].last_name
                    }

                }
              
                 
                $scope.usrname = string
           }  
        });
        }]);



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
                    
                         
              
                  
                   
                  
                   


                 
                    $scope.counter=0;
                    var d = new Date();
                    $scope.monthA = d.getMonth()
                    $scope.yearA = d.getFullYear();
                    $scope.dir ;

                $scope.next = function(n){
                    $scope.dir=n;
                    $scope.counter=$scope.counter+n;
                    
                    $scope.list = document.getElementById("calendar-dates");
                    $scope.c = document.getElementById("calendar-dates").childElementCount;
                    
                   
                    $scope.load(); 
                   
                }
        


$scope.load = function(){
          
    


    var dates = []
    $http.get('/isamm/events/').then(function(response){
      var acts = []

      
      acts = response.data;
      
      
      var i;
      var j;
      for (i = 0; i <  acts.length; i++) {
         var x =  acts[i].date
          dates.push(x)
         
      }
        
      for (j = 0; j <  acts.length; j++) {
           dates[j] =  dates[j].split("-")
            dates[j][0] = parseInt( dates[j][0])
            dates[j][1] = parseInt( dates[j][1])
           dates[j][2] = parseInt( dates[j][2])
           dates[j][3] = acts[j].nom_de_event
          
       }
                            
                            
                        
    
    var month_name = ['January','February','March','April','May','June','July','August','September','October','November','December'];
    if(($scope.monthA-1+$scope.counter)>11&&$scope.dir==1)
    {
        $scope.monthA=1;
        $scope.counter=0;
        $scope.yearA++;

    }
    
    if(($scope.monthA-1+$scope.counter)<0&&$scope.dir==-1)
    {
        $scope.monthA=1;
        $scope.counter=11;
        $scope.yearA--;
    }
    
    var month= $scope.monthA-1+$scope.counter;
    
    var year = $scope.yearA; //2014

                       
           
 
    
   
   
    
    
 
    
    
    
  

    var first_date = month_name[month] + " " + 1 + " " + year;
    //September 1 2014
    var tmp = new Date(first_date).toDateString();
    //Mon Sep 01 2014 ...
    var first_day = tmp.substring(0, 3);    //Mon
    var day_name = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
    var day_no = day_name.indexOf(first_day);   //1
    var days = new Date(year, month+1, 0).getDate();    //30

    
    //Tue Sep 30 2014 ...
    var calendar = get_calendar(day_no, days , month, $scope.yearA,dates );
    document.getElementById("calendar-month-year").innerHTML = month_name[month]+" "+year;
    document.getElementById("calendar-dates").appendChild(calendar);
    
    if($scope.c==2)
    {
      
        $scope.list.removeChild($scope.list.childNodes[0]);
        $scope.list.removeChild($scope.list.childNodes[1]);
     
      
       
    }else{
        $scope.list.removeChild($scope.list.childNodes[1]);
        
    }
});
}

function get_calendar(day_no, days , month,year,dates ){


 
   

    var table = document.createElement('table');

    table.setAttribute("id", "tableA");
    

    
    var tr = document.createElement('tr');
    
    //row for the day letters
    for(var c=0; c<=6; c++){
        var td = document.createElement('td');
        td.innerHTML = "SMTWTFS"[c];
        tr.appendChild(td);
    }
    table.appendChild(tr);
    
    //create 2nd row
    tr = document.createElement('tr');
    var c;
    for(c=0; c<=6; c++){
        if(c == day_no){
            break;
        }
        var td = document.createElement('td');
        td.innerHTML = "";
        
        tr.appendChild(td);
    }
  
    var count = 1;
    for(; c<=6; c++){
        var td = document.createElement('td');
        td.innerHTML = count;
        td.classList.add("Day");
        var k
        for(k=0;k<dates.length;k++)
        {
           if(count==dates[k][2]&&month==Number(dates[k][1]-1)&&year==dates[k][0])
           {
            td.classList.add("activeDay");

            var x = "/isamm/event/"+dates[k][3]+"/";
            td.addEventListener("click", function(){
             window.location.href =x
         });
           }
        
        }
       
          
        
        count++;
        tr.appendChild(td);
    }
    table.appendChild(tr);
     
    //rest of the date rows
 
    

    for(var r=3; r<=7; r++){
        tr = document.createElement('tr');
        for(var c=0; c<=6; c++){
            if(count > days){
                table.appendChild(tr);
                return table;
            }
            
            var td = document.createElement('td');
            td.innerHTML = count;
            
            td.classList.add("Day");
                
              
             for(k=0;k<dates.length;k++)
             {
                if(count==dates[k][2]&&month==Number(dates[k][1]-1)&&year==dates[k][0])
                {
                    td.classList.add("activeDay");
                    
                   var x = "/isamm/event/"+dates[k][3]+"/";
                   td.addEventListener("click", function(){
                    window.location.href =x
                });
                }
                
             }
           
             
             
           
             
           

            count++;
            tr.appendChild(td);
           
            
               
            
        }
        table.appendChild(tr);
         
    
    }
    
    return table;
 
}


                    
                });
                   
                    


    
 
}());