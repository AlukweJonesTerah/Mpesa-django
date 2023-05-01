import React, { Component } from "react";
import { View, Text, TouchableOpacity, Alert } from "react-native";

class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <View
        style={{
          flex: 1,
           borderWidth: 4,
           borderColor: "red",
          marginTop: 10,
          flexDirection: "column",
          marginTop: 20
        }}
      >
        <View
            style={{
                flex:1,
                borderWidth:1,
                borderColor:"Black",
                flexDirection:"row",
                justifyContent:"center",
                alignItems:"center",
                }}>
            <View
                style={{
                    borderWidth:1,
                    borderColor:"green",
                    flex:1.5,
                    justifyContent:"center",
                    alignItems:"center",
                    marginLeft:10,
                    height:50+"%",
                    backgroundColor:"#D2EA9B"
                    }}>
                <Text>I</Text>
            </View>
            <View
                style={{
                    borderWidth:1,
                    borderColor:"green",
                    flex:8.5,
                    marginHorizontal:10,
                    height:50+"%",
                    flexDirection:"row",
                    justifyContent:"flex-start",
                    alignItems:"center",
                    paddingLeft:20,

                    }}>
                <Text>Search product</Text>
            </View>
        </View>
        <View
            style={{
                flex:2,
                borderWidth:1,
                borderColor:"Black",
                }}>
            <Text>Box2</Text>
        </View>
        <View
            style={{
                flex:3,
                borderWidth:1,
                borderColor:"Black",
                }}>
            <Text>Box3</Text>
        </View>
        <View
            style={{
                flex:4,
                borderWidth:1,
                borderColor:"Black",
                }}>
            <Text>Box4</Text>
        </View>
      </View>
    );
  }
}

export default App;
