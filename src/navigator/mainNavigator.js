import React from "react"
import { createDrawerNavigator } from "@react-navigation/drawer"
import { NavigationContainer } from "@react-navigation/native"

import SplashScreen from "../features/SplashScreen"
import SideMenu from "./sideMenu"
//@BlueprintImportInsertion
import UserProfile216921Navigator from '../features/UserProfile216921/navigator';
import Maps216902Navigator from '../features/Maps216902/navigator';
import Settings216880Navigator from '../features/Settings216880/navigator';
import Settings216865Navigator from '../features/Settings216865/navigator';
import NotificationList216864Navigator from '../features/NotificationList216864/navigator';
import Maps216863Navigator from '../features/Maps216863/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {
  //@BlueprintNavigationInsertion
UserProfile216921: { screen: UserProfile216921Navigator },
Maps216902: { screen: Maps216902Navigator },
Settings216880: { screen: Settings216880Navigator },
Settings216865: { screen: Settings216865Navigator },
NotificationList216864: { screen: NotificationList216864Navigator },
Maps216863: { screen: Maps216863Navigator },

  /** new navigators can be added here */
  SplashScreen: {
    screen: SplashScreen
  }
}

const Drawer = createDrawerNavigator()

const AppContainer = () => {
  return (
    <NavigationContainer>
      <Drawer.Navigator drawerContent={props => <SideMenu {...props} />}>
        {Object.keys(AppNavigator).map(s => (
          <Drawer.Screen name={s} component={AppNavigator[s].screen} />
        ))}
      </Drawer.Navigator>
    </NavigationContainer>
  )
}

export default AppContainer
