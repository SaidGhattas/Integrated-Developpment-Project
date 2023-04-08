import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: Home },
        {
            path: '/about/',

            component: () =>
                import ('../views/About.vue')
        },
        {
            path: '/rules',
            name: 'rules',
            component: () =>
                import ('../views/Rules.vue')
        },
        {
            path: '/conditions/services/:id',
            name: 'conditions',
            props: true,
            component: () =>
                import ('../views/Conditions.vue')
        },
        {
            path: '/actions/services/:id',
            name: 'actions',
            props: true,
            component: () =>
                import ('../views/Actions.vue')
        },
        {
            path: '/service/:id/devices/',
            name: 'devices',
            props: true,
            component: () =>
                import ('../views/devices.vue')
        },
        {
            path: '/service/NewDevice/:service_id',
            name: 'NewDevice',
            props: true,
            component: () =>
                import ('../views/NewDevice.vue')
        },
        {
            path: '/service/EditDevice/:service_id/:device_id',
            name: 'EditDevice',
            props: true,
            component: () =>
                import ('../views/EditDevice.vue')
        },
        {
            path: '/service_actions',
            name: 'ServiceActions',
            props: true,
            component: () =>
                import ('../views/ServiceAction.vue')
        },
        {
            path: '/service_actions/:id/devices/',
            name: 'deviceActions',
            props: true,
            component: () =>
                import ('../views/devices_actions.vue')
        }
    ]
})

export default router