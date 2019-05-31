LOCAL_PATH:=$(call my-dir)

include $(CLEAR_VARS)

LOCAL_MODULE:=virtual_multi_inherit_simple

LOCAL_SRC_FILES:=virtual_multi_inherit_simple.cpp

# LOCAL_LDLIBS:=-llog

include $(BUILD_SHARED_LIBRARY)
