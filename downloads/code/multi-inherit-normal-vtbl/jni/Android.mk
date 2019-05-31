LOCAL_PATH:=$(call my-dir)

include $(CLEAR_VARS)

LOCAL_MODULE:=normal_multi_inherit_vtbl

LOCAL_SRC_FILES:=normal_multi_inherit_vtbl.cpp

# LOCAL_LDLIBS:=-llog

include $(BUILD_SHARED_LIBRARY)
