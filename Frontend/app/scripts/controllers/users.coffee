
angular.module('omcktvApp')
  .controller 'UsersCtrl', ($scope, Restangular) ->
    Users = Restangular.all('users')

    Users.getList().then (users) ->
      $scope.users = users

    $scope.newUser = (user) ->
      Users.post(user).then (user) ->
        $scope.users.push(user)

    $scope.deleteUser = (user) ->
      Users.one(user._id).remove().then ->
        $scope.users.pop(user)