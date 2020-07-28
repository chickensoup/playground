/usr/jdk64/jdk1.8.0_77/bin/java -Dzookeeper.log.dir=/var/log/zookeeper -Dzookeeper.log.file=zookeeper-root-server-rndzk02.rnd.fwmrm.net.log -Dzookeeper.root.logger=INFO,ROLLINGFILE -cp /usr/hdp/2.5.3.0-37/zookeeper/bin/../build/classes
/usr/hdp/2.5.3.0-37/zookeeper/bin/../build/lib/*.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/xercesMinimal-1.9.6.2.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/wagon-provider-api-2.4.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/wagon-http-shared4-2.4.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/wagon-http-shared-1.0-beta-6.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/wagon-http-lightweight-1.0-beta-6.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/wagon-http-2.4.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/wagon-file-1.0-beta-6.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/slf4j-log4j12-1.6.1.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/slf4j-api-1.6.1.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/plexus-utils-3.0.8.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/plexus-interpolation-1.11.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/plexus-container-default-1.0-alpha-9-stable-1.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/netty-3.7.0.Final.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/nekohtml-1.9.6.2.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/maven-settings-2.2.1.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/maven-repository-metadata-2.2.1.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/maven-project-2.2.1.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/maven-profile-2.2.1.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/maven-plugin-registry-2.2.1.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/maven-model-2.2.1.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/maven-error-diagnostics-2.2.1.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/maven-artifact-manager-2.2.1.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/maven-artifact-2.2.1.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/maven-ant-tasks-2.1.3.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/log4j-1.2.16.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/jsoup-1.7.1.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/jline-0.9.94.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/commons-logging-1.1.1.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/commons-io-2.2.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/commons-codec-1.6.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/classworlds-1.1-alpha-2.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/backport-util-concurrent-3.1.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/ant-launcher-1.8.0.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../lib/ant-1.8.0.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../zookeeper-3.4.6.2.5.3.0-37.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../src/java/lib/*.jar
/usr/hdp/2.5.3.0-37/zookeeper/bin/../conf

/usr/share/zookeeper/* -Xmx4096m -verbose
gc -XX
+PrintGCDetails -XX
+PrintGCDateStamps -Xloggc
/var/log/zookeeper/zookeeper.gc.201912200105 -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.local.only=false org.apache.zookeeper.server.quorum.QuorumPeerMain /usr/hdp/2.5.3.0-37/zookeeper/bin/../conf/zoo.cfg
