/**
 * Define all of your application routes here
 * for more information on routes, see the
 * official documentation https://router.vuejs.org/en/
 */
export default [
  {
    path: '',
    // Relative to /src/views
    view: 'Dashboard'
  },
  {
    path: '/user-profile',
    name: 'User Profile',
    view: 'UserProfile'
  },
  {
    path: '/currency-list',
    name: 'Currency List',
    view: 'CurrencyList'
  },
  {
    path: '/stock-list',
    view: 'Typography'
  },
  {
    path: '/indices-list',
    view: 'Icons'
  },
  {
    path: '/trend-analysis',
    view: 'Maps'
  },
  {
    path: '/notifications',
    view: 'Notifications'
  },
]
