
angular.module('omcktvApp')
  .controller 'FooterCtrl', ($scope, $modal, Restangular, $rootScope) ->

    Restangular.one('current_user').get().then (
      (user) ->
        $scope.user = user
        return
    ),
    () ->
      user = undefined
      return

    $scope.openLogin = ->
      modalInstance = $modal.open templateUrl: 'views/modals/login.html', controller: 'LoginModal'
      modalInstance.result.then (user) ->
        $scope.user = user;
        return
      return

    $scope.logout = ->
      Restangular.one('logout').get().then (response) ->
        console.log(response)
        $rootScope.broadcast('logout')
        $scope.user = undefined
        return
      return

angular.module('omcktvApp')
  .controller 'LoginModal', ($scope, $modalInstance, Restangular) ->
    $scope.user = {}

    $scope.login = ->
      Restangular.one('login').post('', $scope.user).then (user) ->
        $modalInstance.close(user)
        return
      return