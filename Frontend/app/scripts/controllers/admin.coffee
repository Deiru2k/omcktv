
angular.module('omcktvApp')
  .controller 'AdminCtrl', ($scope, Restangular, $state) ->
    $scope.$on 'logout', ->
      $state.go('main')
      return
    Restangular.one('current_user').get().then ( ->
      $state.go('admin.channels') if $state.current.name == 'admin'
      return
    ), () ->
      $state.go('main')
      return