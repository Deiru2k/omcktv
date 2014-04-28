
angular.module('omcktvApp')
  .controller 'KappaCtrl', ($scope) ->
    $scope.$on '$viewContentLoaded', () ->
      $('#kappa').animate({'height': '1500px'}, 80000)

    $scope.mute = () ->
      player = $('#darude')
      muted = player.prop('muted')
      if muted
        player.prop('muted', false)
      else
        player.prop('muted', true)
      return