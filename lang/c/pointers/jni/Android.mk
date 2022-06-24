LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_MODULE := m
#LOCAL_LDLIBS := -llog
LOCAL_CFLAGS := -fPIE
LOCAL_LDFLAGS := -fPIE -pie
LOCAL_SRC_FILES := m.c

include $(BUILD_EXECUTABLE)
