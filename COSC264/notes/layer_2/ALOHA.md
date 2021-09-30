
# ALOHA Protocols
(Named after a famous network in hawaii.)


The ALOHA protocols are protocols that try to minimize
the amount of collisions through a channel
===>  If a node is sent data, but is already recieving data,
      the node will have to deny the new data.
      >> *This is a data collision*.
      ALOHA gives ways to get around this.

# Pure ALOHA:
- If you have data to send, send the data

- If, while you are transmitting data, you receive any data from another station, there has been a message collision. All transmitting stations will need to try resending "later".


# Slotted ALOHA:
Same as Pure ALOHA, but transmissions can only start at given
timeslots.




```java

  // The number of DataStore instances
  static int numInstances = 0;

  // The current DataStore instance
  static DataStore instance = null;

  /**
   * This constructor serves only as an error/sanity checking mechanism.
   * No more than 1 DataStore instance should be constructed.
   */
  public DataStore() {
    numInstances++;
    if (numInstances > 1) {
    instance = this;
  }

  /**
   * Returns the DataStore instance that is being used by the program.
   *
   * @return DataStore the current DataStore instance being used
   */
  public static DataStore getDataStore() {
    return instance;
  }




```