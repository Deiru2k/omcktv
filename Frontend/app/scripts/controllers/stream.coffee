
angular.module('omcktvApp')
  .controller 'StreamCtrl', ($scope, $stateParams, Restangular, $rootScope) ->
    stream = Restangular.one('channels', $stateParams.channel)
    stream.get().then (channel) ->
      $scope.channel = channel
      $rootScope.active.other = true if !channel.main
      $rootScope.active.other = false if channel.main
      if channel.main
        $rootScope.site_title = channel.name
      else
        $rootScope.site_title = "OmckTV Sidechannel - " + channel.name
      return
    return