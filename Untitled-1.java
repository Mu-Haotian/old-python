/**
 * 校验WLAN配置文件是否正确
 * <p>
 * 校验步骤为：
 * ---step1 添加配置文件
 * ---step3 连接wifi
 * ---step3 ping校验
 */
public synchronized boolean check(String ssid, String password) {
  System.out.println("check : " + password);
  try {
    String profileName = password + ".xml";
    if (addProfile(profileName)) {
      if (connect(ssid)) {
        Thread.sleep(50);
        if (ping()) {
          return true;
        }
      }
    }
  } catch (InterruptedException e) {
    e.printStackTrace();
  }
  return false;
}
/**
 * 添加配置文件
 *
 * @param profileName 添加配置文件
 */
private static boolean addProfile(String profileName) {
  String cmd = Command.ADD_PROFILE.replace("FILE_NAME", profileName);
  List<String> result = execute(cmd, Connector.PROFILE_TEMP_PATH);
  if (result != null && result.size() > 0) {
    if (result.get(0).contains("添加到接口")) {
      return true;
    }
  }
  return false;
}
/**
 * 连接wifi
 *
 * @param ssid 添加配置文件
 */
private static boolean connect(String ssid) {
  boolean connected = false;
  String cmd = Command.CONNECT.replace("SSID_NAME", ssid);
  List<String> result = execute(cmd, null);
  if (result != null && result.size() > 0) {
    if (result.get(0).contains("已成功完成")) {
      connected = true;
    }
  }
  return connected;
}
/**
 * ping 校验
 */
private static boolean ping() {
  boolean pinged = false;
  String cmd = "ping " + Connector.PING_DOMAIN;
  List<String> result = execute(cmd, null);
  if (result != null && result.size() > 0) {
    for (String item : result) {
      if (item.contains("来自")) {
        pinged = true;
        break;
      }
    }
  }
  return pinged;
}


