var myapp = angular.module("myapp", []);
myapp.controller('studentController', function($scope){
$scope.student={
firstName:"Hardik",
lastName:"Dadas",
rollNo:52,
subjects:[
{name:'EH&f', marks:17},
{name:'WebX', marks: 20},
{name:'IOT', marks: 15}
],
fullName:function(){
var studentObject = $scope.student;
return studentObject.firstName+ " "+studentObject.lastName;
}
}
$scope.student={
firstName:"Hardik",
lastName:"Dadas",
rollNo:52,
subjects:[
{name:'EH&f', marks:18},
{name:'WebX', marks: 18},
{name:'IOT', marks: 17}
],
fullName:function(){
var studentObject = $scope.student;
return studentObject.firstName+" "+studentObject.lastName;
}
}})

