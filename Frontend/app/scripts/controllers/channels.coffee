
angular.module('omcktvApp')
  .controller 'ChannelAdmin', ($scope, Restangular) ->

    channels = Restangular.one('channels')
    $scope.new_channel = {'type': 'twitch', main: false}

    channels.get().then (channels) ->
      $scope.channels = channels

    $scope.updateChannel = (channel, $event) ->
      element = $($event.target)
      element.removeClass('btn-success')
      element.removeClass('btn-danger')
      element.addClass('btn-warning')
      channels.one(channel._id).post('', channel).then (() ->
        element.removeClass('btn-warning')
        element.addClass('btn-success')
      ), () ->
        element.removeClass('btn-warning')
        element.addClass('btn-danger')

    $scope.deleteChannel = (channel) ->
      channels.one(channel._id).remove().then () ->
        $scope.channels.other.pop(channel)


    $scope.newChannel = ($event) ->
      element = $($event.target)
      element.removeClass('btn-success')
      element.removeClass('btn-danger')
      element.addClass('btn-warning')
      channels.post('', $scope.new_channel).then (channel) ->
        if channel.main == true
          $scope.channels.main.push(channel)
          element.removeClass('btn-warning')
          element.addClass('btn-success')
        else
          $scope.channels.other.push(channel)
          element.removeClass('btn-warning')
          element.addClass('btn-success')