/**
 * 
 * This script initializes a Vue 3 application that handles URL parameters
 */
const app = {
  data: {
    loading: 0,
    app: '',
    dbname: '',
    tablename: '',
    url: '',
    filter: '',
    order: ''
  },
  methods: {}
};

// Initialize the Vue application
const { createApp } = Vue;

// Create app instance
const initApp = () => {
  app.params = new URLSearchParams(window.location.search);
  app.data.app = app.params.get('app');
  app.data.dbname = app.params.get('dbname');
  app.data.tablename = app.params.get('tablename');
  app.data.url = '../rest/{app}/{dbname}/{tablename}'.format(app.data);
  app.data.filter = app.params.get('filter') || '';
  app.data.order = app.params.get('order') || '';

  // Create Vue 3 app with original data structure
  const vueApp = createApp({
    data() {
      return app.data;
    },
    methods: app.methods
  });

  // Mount the application
  vueApp.mount('#vue');
  
  return vueApp;
};

// Initialize the app
const vueInstance = initApp();