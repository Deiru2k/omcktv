'use strict'

angular.module('omcktvApp', [
  'ngCookies',
  'ngSanitize',
  'ui.router',
  'ui.bootstrap',
  'restangular'
])
.config ($stateProvider, $urlRouterProvider, RestangularProvider) ->
    RestangularProvider.setBaseUrl('/api')
    $urlRouterProvider.otherwise('/')
    $stateProvider
    .state('kappa'; url: '/kappa', templateUrl: 'views/kappa.html', controller: 'KappaCtrl')
    .state('faq'; url: '/faq?faq', templateUrl: 'views/faq.html', controller: 'FaqCtrl')
    .state('main'; url: '/', templateUrl: 'views/main.html', controller: 'MainCtrl')
    .state('main.stream'; url: 'channels/:channel', templateUrl: 'views/stream.html', controller: 'StreamCtrl')
    .state('chat'; url: '/chat', templateUrl: 'views/chat.html')
    .state('html5hd'; url: '/hd5', templateUrl: 'views/html5test.html')
    .state('maraphones'; url: '/maraphones', templateUrl: 'views/maraphones/main.html')
    .state('maraphones.one'; url: '/:maraphone', templateUrl: 'views/maraphones/maraphone.html')
    .state('maraphones.one.record'; url: '/:record', templateUrl: 'views/maraphones/record.html')
    .state('admin'; url: '/admin', templateUrl: 'views/admin/main.html', controller: 'AdminCtrl')
    .state('admin.channels'; url: '/channels', templateUrl: 'views/admin/channels.html', controller: 'ChannelAdmin')
    .state('admin.news'; url: '/news', templateUrl: 'views/admin/news.html', controller: 'NewsAdminCtrl')
    .state('admin.users'; url: '/users', templateUrl: 'views/admin/users.html', controller: 'UsersCtrl')