import Vue from 'vue';
import Router from 'vue-router';
import Games from './components/Games.vue';
import Biblioteca from './components/Biblioteca.vue';
import Ping from './components/Ping.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Biblioteca',
      component: Biblioteca,
    },
    {
      path: '/Games',
      name: 'Games',
      component: Games,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
