
angular.module('omcktvApp')
  .controller 'FaqCtrl', ($scope, $stateParams, $rootScope) ->
    $rootScope.site_title = "OmckTV - FAQ"
    $scope.tab = {}
    if $stateParams.faq == 'maraphone'
      $scope.tab.maraphone = true
    else
      $scope.tab.general = true