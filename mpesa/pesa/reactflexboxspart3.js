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
//                borderWidth:1,
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
                flex:1.85,
//                borderWidth:1,
                borderColor:"Black",
                flexDirection:"row",
                alignItems:"center",
                justifyContent:"flex-start"
                }}>

                <View
                    style = {{
                        width:25+"%",
                        height:70+"%",
                        borderWidth:1,
                        borderColor:"blue",
                        marginRight:20,
                        borderRadius:15,
                        backgroundColor:"#E5F1DB",
                        flexDirection:"column",
                    }}
                    >
                    <View
                        style={{
                            height:75+"%",
                            borderWidth:1,
                            justifyContent:"center",
                            alignItems:"center",
                            borderColor:"red",

                        }}
                        >
                        <Text>IC</Text>
                    </View>

                    <View
                        style={{
                            height:30+"%",
                            borderWidth:1,
                            justifyContent:"center",
                            alignItems:"center",
                            borderColor:"red",

                        }}
                        >

                        <Text>Groceries</Text>
                    </View>

                </View>

                <View
                    style = {{
                        width:25+"%",
                        height:70+"%",
                        borderWidth:1,
                        borderColor:"blue",
                        marginRight:20,
                        borderRadius:15,
                        backgroundColor:"#FEF6E1"
                    }}>

                    <View
                        style={{
                            height:75+"%",
                            borderWidth:1,
                            justifyContent:"center",
                            alignItems:"center",
                            borderColor:"red",

                        }}
                        >
                        <Text>IC</Text>
                    </View>

                      <View
                        style={{
                            height:30+"%",
                            borderWidth:1,
                            justifyContent:"center",
                            alignItems:"center",
                            borderColor:"red",

                        }}
                        >

                       <Text>Repairs</Text>
                    </View>

                </View>

                <View
                    style = {{
                        width:25+"%",
                        height:70+"%",
                        borderWidth:1,
                        borderColor:"blue",
                        marginRight:20,
                        borderRadius:15,
                        backgroundColor:"#D2EA9B"
                    }}>
                    <View
                        style={{
                            height:75+"%",
                            borderWidth:1,
                            justifyContent:"center",
                            alignItems:"center",
                            borderColor:"red",

                        }}
                        >
                        <Text>IC</Text>
                    </View>

                      <View
                        style={{
                            height:30+"%",
                            borderWidth:1,
                            justifyContent:"center",
                            alignItems:"center",
                            borderColor:"red",

                        }}
                        >

                       <Text style={{fontSize:10}}>Gas Deliveries</Text>
                    </View>

                </View>

        </View>


        <View
            style={{
                flex:3.15,
                borderWidth:1,
                borderColor:"black",
                flexDirection:"column",
                justifyContent:"space-between",
                alignItems:"center",
                }}>

                   <View
                         style={{
                                        flex:1,
                                        borderWidth:1,
                                        flexDirection:"row",
                                        justifyContent:"space-between",
                                        alignItems:"center",
                                        borderColor:"blue",
                                        width:100+"%",

                                    }}
                   >
                        <TouchableOpacity
                                    style={{
                                         backgroundColor:"#FC5455",
                                        borderColor:"red",

                                    }} >
                                <Text style={{color:"white",}}>New Products</Text>

                        </TouchableOpacity>

                        <TouchableOpacity
                                style={{
                                    borderColor:"red",

                                }} >

                                <Text style={{color:"#FC5455",}}>See All</Text>
                        </TouchableOpacity>

                   </View>

                    <View
                        style={{
                            flex:9,
                            borderWidth:1,
                            flexDirection:"row",
                            justifyContent:"space-between",
                            alignItems:"center",
                            borderColor:"red",
                        }}>


                          <View
                            style={{
                                flex:1,
                                borderWidth:1,
                                height:80+"%",
                                flexDirection:"column",
                                justifyContent:"space-between",
                                alignItems:"center",
                                borderRadius:10,
                                paddingRight:10,
                                marginRight:10,
                                borderColor:"red",
                                }}>
                                  <View
                                    style={{
                                        flex:1,
//                                        borderWidth:1,
                                        flexDirection:"row",
                                        justifyContent:"flex-end",
                                        }}>
                                        <View style={{  width: 20 +"%",alignSelf:"flex-end"}}>
                                            <Text>heart</Text>
                                        </View>
                                  </View>
                                  <View
                                     style={{
                                        flex:4,
                                        borderWidth:1,
                                        justifyContent:"center",
                                        alignItems:"center",
                                        width:80 +"%",

                                        }}>
                                        <Text>image</Text>
                                  </View>
                                  <View
                                    style={{
                                        flex:3,
//                                        borderWidth:1,
                                        flexDirection:"column",
                                        justifyContent:"flex-start",
                                        alignSelf:"flex-start",
                                        }}>
                                        <Text>Ksh 20</Text>
                                        <Text style={{fontWeight:"bold",}}>Mangoes </Text>
                                        <Text>3</Text>
                                  </View>

                                  <View
                                  style={{
                                        flex:2,
//                                        borderWidth:1,
                                        flexDirection:"row",
                                        justifyContent:"center",
                                        alignItems:"center",
                                        width:100 +"%",
                                        backgroundColor:"#FCBF00",
                                        marginTop:5,
                                        }}>
                                        <Text >Add to cart</Text>
                                  </View>

                            </View>

                        <View
                            style={{
                                flex:1,
                                borderWidth:1,
                                height:80+"%",
                                borderWidth:1,
    //                            justifyContent:"center",
    //                            alignItems:"center",
                                borderColor:"red",
                            }}>
                                  <View>
                                        <Text>h</Text>
                                  </View>
                                  <View>
                                        <Text>image</Text>
                                  </View>

                                  <View>
                                        <Text>Ksh 20</Text>
                                         <Text>Mangoes </Text>
                                          <Text>3</Text>
                                  </View>

                                  <View>
                                        <Text>Add to cart</Text>
                                  </View>
                            <Text>Box3.2</Text>
                        </View>
                 </View>

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
