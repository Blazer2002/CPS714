import homeIcon from './icons/homeButton.png'
import contentIcon from './icons/contentButton.png'
import rewardsIcon from './icons/rewardsButton.png'
import surveyIcon from './icons/surveyButton.png'
import userIcon from './icons/userProfileButton.png'
import settingsIcon from './icons/settingsButton.png'

export const SidebarRef = [
    {
        name: 'Home',
        className: 'sidebar-item',
        path: '/',
        icon: homeIcon
    },
    {
        name: 'Content',
        className: 'sidebar-item',
        path: '/content',
        icon: contentIcon
    },
    {
        name: 'Rewards',
        className: 'sidebar-item',
        path: '/rewards',
        icon: rewardsIcon
    },
    {
        name: 'Survey',
        className: 'sidebar-item',
        path: '/survey',
        icon: surveyIcon
    },
    {
        name: 'Settings',
        className: 'sidebar-item',
        path: '/settings',
        icon: settingsIcon,
        isBottom: true
    },
    {
        name: 'UserProfile',
        className: 'sidebar-item',
        path: '/user',
        icon: userIcon,
        isBottom: true
    }
]