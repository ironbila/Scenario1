function TodoCtrl($scope) {
  
  $scope.todos = [
  ];
  
 // $scope.totalAmount = function () {
   // return $scope.todos.length;
  //};
  
  
  $scope.addstuff = function () {
    $scope.todos.push({text:$scope.formTodoText, done:false});
    $scope.formTodoText = '';
  };
  
    $scope.clearCompleted = function () {
        $scope.todos = _.filter($scope.todos, function(todo){
            return !todo.done;
        });
    };
}