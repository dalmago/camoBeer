/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */

import {
  Text,
  View,
  StyleSheet,
  TextInput,
  Navigator
} from 'react-native';

import React, { Component } from 'react';
import MyScene from './NewScene';

class Beers extends Component {
  constructor(props){
    super(props);

    this.state = { res: '' };
  }

  render(){
    fetch("http://dalmago.xyz:8081/rest/?format=json", {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },

    }).then((res) => res.json()).then((resp) => this.setState({ res: resp.results[0].brand.brand_name })).catch();
    return(
      <Text>Ola {this.state.res}</Text>
    );
  }
}

export class Camobeer extends Component {
  render() {
    return (
      <View style={{flex: 1}}>
        <View style={styles.rec1}>
            <Navigator
            initialRoute={{ title: 'My Initial Scene', index: 0, statusBarHidden: true }}
            renderScene={(route, navigator) =>
              <MyScene
                title={route.title}

                // Function to call when a new scene should be displayed
                onForward={ () => {
                  const nextIndex = route.index + 1;
                  navigator.push({
                    title: 'Scene ' + nextIndex,
                    index: nextIndex,
                  });
                }}

                // Function to call to go back to the previous scene
                onBack={() => {
                  if (route.index > 0) {
                    navigator.pop();
                  }
                }}
              />
            }
          />
        </View>
        <View style={styles.rec2}>
          <TextInput placeholder="type your name here" style={{flex: 1}} />
        </View>
        <View style={styles.rec3}>
          <Beers style={{flex: 1}} />
        </View>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  rec1: {
    flex: 1,
    backgroundColor: 'powderblue',
  },
  rec2: {
    flex: 2,
    backgroundColor: 'skyblue'
  },
  rec3: {
    flex: 3,
    backgroundColor: 'steelblue'
  },
});
