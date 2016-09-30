import { ToggleContainer, ToggleItem } from 'deco-ride-share-demo'
import React, { Component } from 'react';
import {
  View,
  Text,
  TouchableOpacity,
  TextInput,
} from 'react-native'

export default class MyScene extends Component {
  static get defaultProps() {
    return {
      title: 'MyScene'
    };
  }

  render() {
    return (
      <View>
        <Text>Current Scene: { this.props.title }</Text>
        <TouchableOpacity onPress={this.props.onForward}>
          <Text>Tap me to load the next scene</Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={this.props.onBack}>
          <Text>Tap me to go back</Text>
        </TouchableOpacity>
      </View>
    )
  }
}
