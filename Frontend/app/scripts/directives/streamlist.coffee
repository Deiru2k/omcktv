
angular.module('omcktvApp')
  .directive 'streamlist', ($rootScope) ->
    return restrict: 'A',
    scope: true,
    templateUrl: 'views/directives/streamlist.html',
    controller: ($scope, $stateParams) ->
      $scope.setActive = (channel) ->
        $scope.active_channel = channel
        return
      $scope.$watch 'channels.other', (channels) ->
        channels.forEach (channel) ->
          if channel._id == $stateParams.stream
            $scope.active_channel = channel
          return
        return