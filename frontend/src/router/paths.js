/**
 * Define all of your application routes here
 * for more information on routes, see the
 * official documentation https://router.vuejs.org/en/
 */
export default [
  {
    path: '',
    // Relative to /src/views
    name: 'Your Daily Finances',
    view: 'Dashboard'
  },
  {
    path: '/user-profile',
    name: 'User Profile',
    view: 'UserProfile'
  },
  {
    path: '/cryptocurrency-list',
    name: 'Cryptocurrency List',
    view: 'CryptoList'
  },
  {
    path: '/stock-list',
    name: 'Stock List',
    view: 'StockList'
  },
  {
    path: '/indices-list',
    name: 'Indice List',
    view: 'IndiceList'
  },
  {
    path: '/trend-analysis',
    name: 'Trend Analysis',
    view: 'Maps'
  },
  {
    path: '/notifications',
    name: 'Notifications',
    view: 'Notifications'
  },
]
