'use strict'

angular.module('omcktvApp')
  .controller 'MainCtrl', ($scope, Restangular, $interval, $state, $cookieStore, $rootScope) ->
    $rootScope.active = {}
    $state.go('main.stream'; channel: 'livestream') if $state.current.name != 'main.stream'
    if $cookieStore.get('background') != undefined
      $scope.background = $cookieStore.get('background')
    else
      $scope.background = false

    if $scope.background
      $('body').addClass('bg')
    else
      $('body').addClass('nobg')
    $scope.chat = true
    $scope.schedule = false
    channels = Restangular.one('channels')
    news = Restangular.all('news')
    $scope.toggleBackground = ->
      if $scope.background
        $('body').addClass('nobg')
        $('body').removeClass('bg')
        $scope.background = false
      else
        $('body').removeClass('nobg')
        $('body').addClass('bg')
        $scope.background = true
      return
    $scope.$watch 'background', (background) ->
      $cookieStore.put('background', background)
    $scope.toggleSchedule = ->
      $scope.schedule = !$scope.schedule
    $scope.popupChat = ->
      $scope.chat = false
      window.open('/#/chat','OmckTV Chat','width=500,height=800,toolbar=0,menubar=0,location=0,status=1,scrollbars=0,resizable=1,left=0,top=0');
      return
    $scope.toggleChat = ->
      $scope.chat = !$scope.chat
      return
    update = ->
      channels.get({'live': true}).then (list) ->
        $scope.channels = list
        return
      return
    update()
    $interval(update, 30000)
    return