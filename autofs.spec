#
# $Id: autofs.spec,v 1.11 2003/12/04 15:41:32 raven Exp $
#
# Use --without systemd in your rpmbuild command or force values to 0 to
# disable them.
%define with_systemd        %{?_without_systemd:        0} %{?!_without_systemd:        1}

Summary: A tool for automatically mounting and unmounting filesystems
Name: autofs
Version: 5.0.7
Release: 83%{?dist}
Epoch: 1
License: GPLv2+
Group: System Environment/Daemons
Source: ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/autofs-%{version}.tar.bz2
Patch1: autofs-5.0.7-fix-nobind-sun-escaped-map-entries.patch
Patch2: autofs-5.0.7-fix-use-cache-entry-after-free-mistake.patch
Patch3: autofs-5.0.7-fix-ipv6-proximity-calculation.patch
Patch4: autofs-5.0.7-fix-parse-buffer-initialization.patch
Patch5: autofs-5.0.7-fix-typo-in-automount-8.patch
Patch6: autofs-5.0.7-include-usage-in-usage-message.patch
Patch7: autofs-5.0.7-dont-wait-forever-to-restart.patch
Patch8: autofs-5.0.7-add-timeout-option-description-to-man-page.patch
Patch9: autofs-5.0.7-fix-null-map-entry-order-handling.patch
Patch10: autofs-5.0.7-make-description-of-default-MOUNT_WAIT-setting-clear.patch
Patch11: autofs-5.0.7-configure-in-allow-cross-compilation.patch
Patch12: autofs-5.0.7-README-update-mailing-list-subscription-info.patch
Patch13: autofs-5.0.7-allow-non-root-user-to-check-status.patch
Patch14: autofs-5.0.7-configure-allow-cross-compilation-update.patch
Patch15: autofs-5.0.6-fix-recursive-mount-deadlock.patch
Patch16: autofs-5.0.6-increase-file-map-read-buffer-size.patch
Patch17: autofs-5.0.7-handle-new-location-of-systemd.patch
Patch18: autofs-5.0.7-fix-map-entry-duplicate-offset-detection.patch
Patch19: autofs-5.0.7-allow-nsswitch_conf-to-not-contain-automount-lines.patch
Patch20: autofs-5.0.7-fix-nobind-man-page-description.patch
Patch21: autofs-5.0.7-fix-submount-offset-delete.patch
Patch22: autofs-5.0.7-fix-init-script-status-return.patch
Patch23: autofs-5.0.7-fix-use-get_proximity-without-libtirpc.patch
Patch24: autofs-5.0.7-dont-use-dirent-d_type-to-filter-out-files-in-scandir.patch
Patch25: autofs-5.0.7-dont-schedule-new-alarms-after-readmap.patch
Patch26: autofs-5.0.7-use-numeric-protocol-ids-instead-of-protoent-structs.patch
Patch27: autofs-5.0.7-lib-defaults-use-WITH_LDAP-conditional-around-LDAP-types.patch
Patch28: autofs-5.0.7-make-yellow-pages-support-optional.patch
Patch29: autofs-5.0.7-modules-replicated-use-sin6.addr-s6_addr32.patch
Patch30: autofs-5.0.7-workaround-missing-GNU-versionsort-extension.patch
Patch31: autofs-5.0.7-dont-fail-on-master-map-self-include.patch
Patch32: autofs-5.0.7-fix-wildcard-multi-map-regression.patch
Patch33: autofs-5.0.7-fix-file-descriptor-leak-when-reloading-the-daemon.patch
Patch34: autofs-5.0.7-depricate-nosymlink-pseudo-option.patch
Patch35: autofs-5.0.7-add-symlink-pseudo-option.patch
Patch36: autofs-5.0.7-update-kernel-include-files.patch
Patch37: autofs-5.0.7-fix-requires-in-spec-file.patch
Patch38: autofs-5.0.7-fix-libtirpc-build-option.patch
Patch39: autofs-5.0.7-fix-systemd-unidir-in-spec-file.patch
Patch40: autofs-5.0.7-document-browse-option-in-man-page.patch
Patch41: autofs-5.0.7-fix-automounter-support-on-parisc.patch
Patch42: autofs-5.0.7-fix-some-automount_8-typos.patch
Patch43: autofs-5.0.7-syncronize-handle_mounts-shutdown.patch
Patch44: autofs-5.0.7-fix-submount-tree-not-all-expiring.patch
Patch45: autofs-5.0.7-make-dump-maps-check-for-duplicate-indirect-mounts.patch
Patch46: autofs-5.0.7-document-allowed-map-sources-in-auto_master.patch
Patch47: autofs-5.0.7-add-enable-sloppy-mount-option-to-configure.patch
Patch48: autofs-5.0.7-fix-interface-address-null-check.patch
Patch49: autofs-5.0.7-dont-probe-rdma-mounts.patch
Patch50: autofs-5.0.7-fix-master-map-mount-options-matching.patch
Patch51: autofs-5.0.7-fix-master-map-bogus-keywork-match.patch
Patch52: autofs-5.0.7-fix-fix-map-entry-duplicate-offset-detection.patch
Patch53: autofs-5.0.7-probe-each-nfs-version-in-turn-for-singleton-mounts.patch
Patch54: autofs-5.0.7-fix-fcntl-return-check.patch
Patch55: autofs-5.0.7-fix-spawn_umount-return-check-in-mount_bind-lookup_init.patch
Patch56: autofs-5.0.7-fix-check-mkdir_path-in-mount_bind-mount_mount.patch
Patch57: autofs-5.0.7-fix-incorrect-name-in-test.patch
Patch58: autofs-5.0.7-remove-debug-only-code-in-alarm-c.patch
Patch59: autofs-5.0.7-fix-inconsistent-use-of-cache-lock-in-handle_packet_missing_direct.patch
Patch60: autofs-5.0.7-fix-several-off-by-one-errors.patch
Patch61: autofs-5.0.7-fix-memory-leak-in-get_dc_list.patch
Patch62: autofs-5.0.7-fix-host_addr-null-reference-in-add_new_host.patch
Patch63: autofs-5.0.7-add-null-check-in-read_one.patch
Patch64: autofs-5.0.7-add-pgrp-check-in-do_spawn.patch
Patch65: autofs-5.0.7-fix-inconsistent-signed-usage-for-__rpc_ping.patch
Patch66: autofs-5.0.7-add-null-check-in-extract_version.patch
Patch67: autofs-5.0.7-recheck-valid-map-entry-lookup-return-in-do_readmap_mount.patch
Patch68: autofs-5.0.7-add-null-check-in-parse_server_string.patch
Patch69: autofs-5.0.7-add-map-entry-null-check-in-do_expire_direct.patch
Patch70: autofs-5.0.7-add-mapent-null-check-in-lookup-nisplus-lookup_mount.patch
Patch71: autofs-5.0.7-fix-potential-null-dereference-in-lookup_mount.patch
Patch72: autofs-5.0.7-fix-leaked-ldap-percent-hack-allocation-in-lookup_one.patch
Patch73: autofs-5.0.7-fix-incorrect-value-reference-in-parse_line.patch
Patch74: autofs-5.0.7-add-debug-alert-for-waitpid-in-check_nfs_mount_version.patch
Patch75: autofs-5.0.7-add-initialization-of-bind_result-in.patch-do_sasl_bind.patch
Patch76: autofs-5.0.7-fix-incorrect-check-in-flag_is_owned.patch
Patch77: autofs-5.0.7-fix-possible-use-after-free-in-lookup_dir-lookup_init.patch
Patch78: autofs-5.0.7-add-changlog-entry-for-coverity-fixes.patch
Patch79: autofs-5.0.7-fix-probe-each-nfs-version-in-turn-for-singleton-mounts.patch
Patch80: autofs-5.0.7-misc-man-page-fixes.patch
Patch81: autofs-5.0.7-fix-add-null-check-in-parse_server_string.patch
Patch82: autofs-5.0.7-check-for-protocol-option.patch
Patch83: autofs-5.0.7-use-ulimit-max-open-files-if-greater-than-internal-maximum.patch
Patch84: autofs-5.0.7-dont-override-LDFLAGS-in-make-rules.patch
Patch85: autofs-5.0.7-fix-a-couple-of-compiler-warnings.patch
Patch86: autofs-5.0.7-add-after-sssd-dependency-to-unit-file.patch
Patch87: autofs-5.0.7-fix-syncronize-handle_mounts-shutdown.patch
Patch88: autofs-5.0.7-fix-fix-wildcard-multi-map-regression.patch
Patch89: autofs-5.0.7-fix-dumpmaps-multi-output.patch
Patch90: autofs-5.0.7-try-and-cleanup-after-dumpmaps.patch
Patch91: autofs-5.0.7-teach-dumpmaps-to-output-simple-key-value-pairs.patch
Patch92: autofs-5.0.7-fix-get_nfs_info-probe.patch
Patch93: autofs-5.0.7-fix-portmap-lookup.patch
Patch94: autofs-5.0.7-only-probe-specific-nfs-version-when-requested.patch
Patch95: autofs-5.0.8-fix-ipv6-libtirpc-getport.patch
Patch96: autofs-5.0.7-improve-timeout-option-description.patch
Patch97: autofs-5.0.8-fix-ipv6-link-local-address-handling.patch
Patch98: autofs-5.0.8-fix-fix-ipv6-libtirpc-getport.patch
Patch99: autofs-5.0.8-get_nfs_info-should-query-portmapper-if-port-is-not-given.patch
Patch100: autofs-5.0.8-fix-ipv6-libtirpc-getport-proto-not-set.patch
Patch101: autofs-5.0.8-fix-portmap-not-trying-proto-v2.patch
Patch102: autofs-5.0.8-fix-negative-status-being-reset-on-map-read.patch
Patch103: autofs-5.0.9-fix-fix-negative-status-being-reset-on-map-read.patch
Patch104: autofs-5.0.9-check-for-non-existent-negative-entries-in-lookup_ghost.patch
Patch105: autofs-5.0.7-allow-use-of-hosts-map-in-maps.patch
Patch106: autofs-5.0.8-fix-options-compare.patch
Patch107: autofs-5.0.8-fix-fix-options-compare.patch

# pre-patches for amd parser series.
Patch400: autofs-5.0.8-fix-max-declaration.patch
Patch401: autofs-5.0.7-setup-program-map-env-from-macro-table.patch
Patch402: autofs-5.0.7-add-short-host-name-standard-marco-variable.patch
Patch403: autofs-5.0.8-fix-symlink-fail-message-in-mount_bind-c.patch
Patch404: autofs-5.0.7-add-std-vars-to-program-map-invocation.patch
Patch405: autofs-5.0.8-check-for-existing-offset-mount-before-mounting.patch
Patch406: autofs-5.0.8-remove-macro-debug-prints.patch
Patch407: autofs-5.0.8-fix-cache-readlock-not-taken-on-lookup.patch
Patch408: autofs-5.0.7-fix-compilation-of-lookup_ldap_c-without-sasl.patch
Patch409: autofs-5.0.8-fix-undefined-authtype_requires_creds-err-if-ldap-en.patch
Patch410: autofs-5.0.8-pass-map_source-as-function-paramter-where-possible.patch
Patch411: autofs-5.0.8-check-for-bind-onto-self-in-mount_bind-c.patch
Patch412: autofs-5.0.8-fix-symlink-expire.patch
Patch413: autofs-5.0.8-fix-master-map-type-check.patch
Patch414: autofs-5.0.8-dont-clobber-mapent-for-negative-cache.patch
Patch415: autofs-5.0.7-fix-bad-mkdir-permission-on-create.patch
Patch416: autofs-5.0.8-fix-macro_addvar-and-move-init-to-main-thread.patch
Patch417: autofs-5.0.8-change-walk_tree-to-take-ap.patch
Patch418: autofs-5.0.8-add-negative-cache-lookup-to-hesiod-lookup.patch
Patch419: autofs-5.0.8-fix-external-env-configure.patch
Patch420: autofs-5.0.8-make-autofs-5-consistent-with-auto-master-5.patch
Patch421: autofs-5.0.8-fix-map-source-with-type-lookup.patch
Patch422: autofs-5.0.8-fix-fix-map-source-with-type-lookup.patch
Patch423: autofs-5.0.8-fix-lookup_nss_mount-map-lookup.patch
Patch424: autofs-5.0.8-dont-ignore-null-cache-entries-on-multi-mount-umount.patch
Patch425: autofs-5.0.8-fix-inconsistent-error-returns-in-handle_packet_missing_direct.patch
Patch426: autofs-5.0.8-simple-coverity-fixes.patch
Patch427: autofs-5.0.8-remove-stale-debug-message.patch
Patch428: autofs-5.0.8-fixes-for-samples-auto_master.patch
Patch429: autofs-5.0.8-fix-variable-substitution-description.patch
Patch430: autofs-5.0.8-fix-append-options-description-in-README_v5-release.patch
Patch431: autofs-5.0.9-fix-mistake-in-assignment.patch
Patch432: autofs-5.0.8-use-open-instead-of-access.patch
Patch433: autofs-5.0.7-fix-crash-due-to-thread-unsafe-use-of-libldap.patch
Patch434: autofs-5.0.8-fix-deadlock-in-init-ldap-connection.patch
Patch435: autofs-5.0.8-extend-libldap-serialization.patch

# amd parser series (set1)
Patch500: autofs-5.0.9-amd-lookup-move-get_proximity-to-parse_subs-c.patch
Patch501: autofs-5.0.9-amd-lookup-use-flags-in-map_source-for-format.patch
Patch502: autofs-5.0.9-amd-lookup-rework-config-handling.patch
Patch503: autofs-5.0.9-amd-lookup-add-conf-handling-for-amd-maps.patch
Patch504: autofs-5.0.9-amd-lookup-split-config-into-init-and-config-settings.patch
Patch505: autofs-5.0.9-amd-lookup-update-man-page-autofs-config-description.patch
Patch506: autofs-5.0.9-amd-lookup-add-amd-config-descriptions-to-config.patch
Patch507: autofs-5.0.9-amd-lookup-fix-lofs-mounting.patch
Patch508: autofs-5.0.9-amd-lookup-add-merge_options-function.patch
Patch509: autofs-5.0.9-amd-lookup-add-expandamdent-function.patch
Patch510: autofs-5.0.9-amd-lookup-add-external-mounts-tracking-functions.patch
Patch511: autofs-5.0.9-amd-lookup-add-amd-global-macro-vars.patch
Patch512: autofs-5.0.9-amd-lookup-add-selector-handling-functions.patch
Patch513: autofs-5.0.9-amd-lookup-add-parse_amd-c.patch
Patch514: autofs-5.0.9-amd-lookup-add-parent-prefix-handling.patch
Patch515: autofs-5.0.9-amd-lookup-add-lookup-vars.patch
Patch516: autofs-5.0.9-amd-lookup-add-selector-handling.patch
Patch517: autofs-5.0.9-amd-lookup-add-cut-handling.patch
Patch518: autofs-5.0.9-amd-lookup-add-handling-of-amd-maps-in-the-master-map.patch
Patch519: autofs-5.0.9-amd-lookup-add-cache-partial-match-functions.patch
Patch520: autofs-5.0.9-amd-lookup-fix-expire-of-amd-nfs-mounts.patch
Patch521: autofs-5.0.9-amd-lookup-add-lofs-ext-and-xfs-fs-types.patch
Patch522: autofs-5.0.9-amd-lookup-add-key-matching-helper-function.patch
Patch523: autofs-5.0.9-amd-lookup-update-lookup-file-to-handle-amd-keys.patch
Patch524: autofs-5.0.9-amd-lookup-update-lookup-yp-to-handle-amd-keys.patch
Patch525: autofs-5.0.9-amd-lookup-update-lookup-program-to-handle-amd-keys.patch
Patch526: autofs-5.0.9-amd-lookup-update-lookup-nisplus-to-handle-amd-keys.patch
Patch527: autofs-5.0.8-amd-lookup-update-lookup-ldap-to-handle-amd-keys.patch
Patch528: autofs-5.0.8-amd-lookup-update-lookup-hesiod-to-handle-amd-keys.patch
Patch529: autofs-5.0.9-amd-lookup-add-handling-of-unhandled-options.patch
Patch530: autofs-5.0.9-amd-lookup-use-config-map_type-if-type-is-not-given.patch
Patch531: autofs-5.0.9-amd-lookup-update-man-pages.patch
Patch532: autofs-5.0.9-amd-lookup-add-remopts-handling.patch
Patch533: autofs-5.0.9-amd-lookup-add-nfsl-and-linkx-fs-types.patch
Patch534: autofs-5.0.9-amd-lookup-add-search_path-handling.patch
Patch535: autofs-5.0.9-amd-lookup-fix-host-mount-lookup.patch
Patch536: autofs-5.0.9-amd-lookup-fix-host-mount-naming.patch
Patch537: autofs-5.0.9-amd-lookup-check-for-required-options-for-mounts.patch
Patch538: autofs-5.0.9-amd-lookup-add-cdfs-fs-type.patch
Patch539: autofs-5.0.9-amd-lookup-dont-umount-admin-mounted-external-mounts.patch
Patch540: autofs-5.0.9-amd-lookup-skip-sss-source-for-amd-lookups.patch
Patch541: autofs-5.0.9-amd-lookup-allow-exec-to-be-used-by-amd-maps-in-master-map.patch
Patch542: autofs-5.0.9-amd-lookup-fix-amd-entry-not-found-at-expire.patch
Patch543: autofs-5.0.9-amd-lookup-fix-prefix-not-set-on-mount-reconnect.patch
Patch544: autofs-5.0.9-amd-lookup-add-REDAME-amd-maps.patch
Patch545: autofs-5.0.9-amd-lookup-fix-autofs_use_lofs-value-in-config.patch
Patch546: autofs-5.0.9-amd-lookup-fix-expire-of-external-mounts.patch
Patch547: autofs-5.0.9-amd-lookup-try-to-use-external-mounts-for-real-mounts.patch
Patch548: autofs-5.0.9-amd-lookup-add-ufs-fs-type.patch
Patch549: autofs-5.0.9-amd-lookup-fix-old-conf-handling.patch
Patch550: autofs-5.0.9-amd-lookup-try-to-use-external-mounts-for-nfs-mounts.patch
Patch551: autofs-5.0.9-amd-lookup-update-changelog.patch

# amd parser series (set2)
Patch552: autofs-5.1.0-beta1-fix-wildcard-key-lookup.patch
Patch553: autofs-5.1.0-beta1-fix-out-of-order-amd-timestamp-lookup.patch
Patch554: autofs-5.1.0-beta1-fix-ldap-default-schema-config.patch
Patch555: autofs-5.1.0-beta1-fix-ldap-default-master-map-name-config.patch
Patch556: autofs-5.1.0-beta1-fix-map-format-init-in-lookup_init.patch
Patch557: autofs-5.1.0-beta1-fix-incorrect-max-key-length-in-defaults-get_hash.patch
Patch558: autofs-5.1.0-beta1-fix-xfn-sets-incorrect-lexer-state.patch
Patch559: autofs-5.1.0-beta1-fix-old-style-key-lookup.patch
Patch560: autofs-5.1.0-beta1-fix-expire-when-server-not-responding.patch
Patch561: autofs-5.1.0-beta1-fix-ldap_uri-config-update.patch
Patch562: autofs-5.1.0-beta1-fix-typo-in-conf_load_autofs_defaults.patch
Patch563: autofs-5.1.0-beta1-fix-hash-on-config-option-add-and-delete.patch
Patch564: autofs-5.1.0-beta1-add-plus-to-path-match-pattern.patch
Patch565: autofs-5.1.0-beta1-fix-multi-entry-ldap-option-handling.patch
Patch566: autofs-5.1.0-beta1-cleanup-options-in-amd_parse-c.patch
Patch567: autofs-5.1.0-beta1-allow-empty-value-for-some-map-options.patch
Patch568: autofs-5.1.0-beta1-allow-empty-value-in-macro-selectors.patch

Patch600: autofs-5.1.0-add-serialization-to-sasl-init.patch
Patch601: autofs-5.1.0-dont-allocate-dev_ctl_ops-too-early.patch
Patch602: autofs-5.1.0-fix-incorrect-round-robin-host-detection.patch
Patch603: autofs-5.0.9-fix-race-accessing-qdn-in-get_query_dn.patch

# Coverity motivated fixes, mainly for the new amd parser code
Patch604: autofs-5.1.0-fix-leak-in-cache_push_mapent.patch
Patch605: autofs-5.1.0-fix-config-entry-read-buffer-not-checked.patch
Patch606: autofs-5.1.0-fix-FILE-pointer-check-in-defaults_read_config.patch
Patch607: autofs-5.1.0-fix-memory-leak-in-conf_amd_get_log_options.patch
Patch608: autofs-5.1.0-fix-signed-comparison-in-inet_fill_net.patch
Patch609: autofs-5.1.0-fix-buffer-size-checks-in-get_network_proximity.patch
Patch610: autofs-5.1.0-fix-leak-in-get_network_proximity.patch
Patch611: autofs-5.1.0-fix-buffer-size-checks-in-merge_options.patch
Patch612: autofs-5.1.0-check-amd-lex-buffer-len-before-copy.patch
Patch613: autofs-5.1.0-add-return-check-in-ldap-check_map_indirect.patch
Patch614: autofs-5.1.0-check-host-macro-is-set-before-use.patch
Patch615: autofs-5.1.0-check-options-length-before-use-in-parse_amd_c.patch
Patch616: autofs-5.1.0-fix-some-out-of-order-evaluations-in-parse_amd_c.patch
Patch617: autofs-5.1.0-fix-copy-and-paste-error-in-dup_defaults_entry.patch
Patch618: autofs-5.1.0-fix-leak-in-parse_mount.patch
Patch619: autofs-5.1.0-add-mutex-call-return-check-in-defaults_c.patch

# more amd format map fixes
Patch620: autofs-5.1.0-force-disable-browse-mode-for-amd-format-maps.patch
Patch621: autofs-5.1.0-fix-hosts-map-options-check-in-lookup_amd_instance.patch

Patch622: autofs-5.1.0-fix-mem-leak-in-create_client.patch
Patch623: autofs-5.1.0-fix-memory-leak-in-get_exports.patch

Patch624: autofs-5.1.0-fix-memory-leak-in-get_defaults_entry.patch
Patch625: autofs-5.1.0-fix-out-of-order-clearing-of-options-buffer.patch
Patch626: autofs-5.1.0-fix-reset-amd-lexer-scan-buffer.patch
Patch627: autofs-5.1.0-ignore-multiple-commas-in-options-strings.patch

Patch628: autofs-5.1.0-clarify-multiple-mounts-description.patch
Patch629: autofs-5.1.0-update-man-page-autofs-8-for-systemd.patch
Patch630: autofs-5.1.0-fix-fix-master-map-type-check.patch
Patch631: autofs-5.1.0-fix-typo-in-update_hosts_mounts.patch
Patch632: autofs-5.1.0-fix-hosts-map-update-on-reload.patch
Patch633: autofs-5.1.0-make-negative-cache-update-consistent-for-all-lookup-modules.patch
Patch634: autofs-5.1.0-ensure-negative-cache-isnt-updated-on-remount.patch
Patch635: autofs-5.1.0-dont-add-wildcard-to-negative-cache.patch
Patch636: autofs-5.1.0-add-a-prefix-to-program-map-stdvars.patch
Patch637: autofs-5.1.0-add-config-option-to-force-use-of-program-map-stdvars.patch
Patch638: autofs-5.1.0-fix-incorrect-check-in-parse_mount.patch
Patch639: autofs-5.1.0-handle-duplicates-in-multi-mounts.patch
Patch640: autofs-5.1.0-fix-macro-usage-in-lookup_program_c.patch
Patch641: autofs-5.1.0-remove-unused-offset-handling-code.patch
Patch642: autofs-5.1.0-fix-mount-as-you-go-offset-selection.patch

Patch643: autofs-5.1.0-init-qdn-before-use.patch
Patch644: autofs-5.1.1-fix-left-mount-count-return.patch
Patch645: autofs-5.1.1-fix-return-handling-in-sss-lookup-module.patch
Patch646: autofs-5.1.1-move-query-dn-calculation-from-do_bind-to-do_connect.patch
Patch647: autofs-5.1.1-make-do_connect-return-a-status.patch
Patch648: autofs-5.1.1-make-connect_to_server-return-a-status.patch
Patch649: autofs-5.1.1-make-find_dc_server-return-a-status.patch
Patch650: autofs-5.1.1-make-find_server-return-a-status.patch
Patch651: autofs-5.1.1-fix-return-handling-of-do_reconnect-in-ldap-module.patch
Patch652: autofs-5.1.1-fix-direct-mount-stale-instance-flag-reset.patch
Patch653: autofs-5.1.1-fix-direct-map-expire-not-set-for-initial-empty-map.patch
Patch654: autofs-5.1.1-update-map_hash_table_size-description.patch
Patch655: autofs-5.1.1-fix-out-of-order-call-in-program-map-lookup.patch

Patch700: autofs-5.1.0-make-service-want-network-online.patch
Patch701: autofs-5.1.1-add-remote-fs-target-systemd-dependency.patch
Patch702: autofs-5.0.9-revert-special-case-cifs-escapes.patch
Patch703: autofs-5.1.0-guard-against-incorrect-umount-return.patch
Patch704: autofs-5.1.1-fix-nameing-typo-in-autofs-conf.patch

Patch705: autofs-5.1.1-always-set-direct-mounts-catatonic-at-exit.patch
Patch706: autofs-5.1.1-log-pipe-read-errors.patch
Patch707: autofs-5.1.1-fix-rwlock-unlock-crash.patch
Patch708: autofs-5.1.1-fix-handle_mounts-termination-condition-check.patch

# Series 1 - additional bug fixes (bug 1300500)
Patch709: autofs-5.1.1-fix-config-old-name-lookup.patch
Patch710: autofs-5.1.1-fix-error-handling-on-ldap-bind-fail.patch
Patch711: autofs-5.1.0-fix-gcc5-complaints.patch
Patch712: autofs-5.1.1-fix-fix-gcc5-complaints.patch

# Series2 - add reinit method and change lookup to use reinit
# instead of reopen (bug 1300500)
Patch713: autofs-5.1.1-fix-missing-source-sss-in-multi-map-lookup.patch
Patch714: autofs-5.1.1-fix-update_hosts_mounts-return.patch
Patch715: autofs-5.1.1-move-check_nss_result-to-nsswitch_c.patch
Patch716: autofs-5.1.1-make-open_lookup-return-nss-status.patch
Patch717: autofs-5.1.1-fix-nsswitch-handling-when-opening-multi-map.patch
Patch718: autofs-5.1.1-add-reinit-entry-point-to-modules.patch
Patch719: autofs-5.1.1-implement-reinit-in-parse-modules.patch
Patch720: autofs-5.1.1-implement-reinit-in-file-lookup-module.patch
Patch721: autofs-5.1.1-implement-reinit-in-hesiod-lookup-module.patch
Patch722: autofs-5.1.1-implement-reinit-in-hosts-lookup-module.patch
Patch723: autofs-5.1.1-implement-reinit-in-ldap-lookup-module.patch
Patch724: autofs-5.1.1-implement-reinit-in-nisplus-lookup-module.patch
Patch725: autofs-5.1.1-implement-reinit-in-program-lookup-module.patch
Patch726: autofs-5.1.1-implement-reinit-in-sss-lookup-module.patch
Patch727: autofs-5.1.1-implement-reinit-in-yp-lookup-module.patch
Patch728: autofs-5.1.1-add-type-to-struct-lookup_mod.patch
Patch729: autofs-5.1.1-factor-out-free-multi-map-context.patch
Patch730: autofs-5.1.1-factor-out-alloc-multi-map-context.patch
Patch731: autofs-5.1.1-fix-map-format-check-in-nss_open_lookup-multi-map-module.patch
Patch732: autofs-5.1.1-implement-reinit-in-multi-lookup-module.patch
Patch733: autofs-5.1.1-change-lookup-to-use-reinit-instead-of-reopen.patch

# Aditional bug fixes (bug 1300500)
Patch734: autofs-5.1.1-fix-unbind-external-mech.patch
Patch735: autofs-5.1.1-fix-sasl-connection-concurrancy-problem.patch

# Some Coverity fixes identified for recent changes (bug 1300500)
Patch736: autofs-5.1.1-fix-memory-leak-in-nisplus-lookup_reinit.patch
Patch737: autofs-5.1.1-fix-memory-leak-in-ldap-do_init.patch
Patch738: autofs-5.1.1-fix-use-after-free-in-sun-parser-parse_init.patch
Patch739: autofs-5.1.1-fix-use-after-free-in-open_lookup.patch
Patch740: autofs-5.1.1-fix-typo-in-autofs_sasl_bind.patch

Patch741: autofs-5.1.1-add-configuration-option-to-use-hostname-in-mounts.patch
Patch742: autofs-5.1.1-fix-use-after-free-st_queue_handler.patch
Patch743: autofs-5.1.1-add-config-option-to-suppress-not-found-log-message.patch

Patch744: autofs-5.1.2-wait-for-master-map-available-at-start.patch
Patch745: autofs-5.1.2-add-master-read-wait-option.patch
Patch746: autofs-5.1.2-fix-included-master-map-not-found-return.patch
Patch747: autofs-5.1.2-dont-fail-on-master-map-read-fail-timeout.patch
Patch748: autofs-5.1.2-set-sane-default-master-read-wait-timeout.patch
Patch749: autofs-5.1.2-dont-return-until-after-master-map-retry-read.patch
Patch750: autofs-5.1.2-make-lookup_nss_read_master-return-nss-status.patch

Patch751: autofs-5.1.2-make-set_direct_mount_catatonic-more-general.patch
Patch752: autofs-5.1.2-set-autofs-mounts-catatonic-at-exit.patch
Patch753: autofs-5.1.2-check-NFS-server-availability-on-local-mount-fallback.patch
Patch754: autofs-5.1.2-honor-last-rw-in-mount-options-when-doing-a-bind-mount.patch
Patch755: autofs-5.1.2-update-and-add-README-for-old-autofs-schema.patch

# Bug 1367576 - amd mounts browse mode
Patch760: autofs-5.1.2-fix-short-memory-allocation-in-lookup_amd_instance.patch
Patch761: autofs-5.1.2-fix-count_mounts-function.patch
Patch762: autofs-5.1.2-fix-argc-off-by-one-in-mount_autofs_c.patch
Patch763: autofs-5.1.2-fix-_strncmp-usage.patch
Patch764: autofs-5.1.2-fix-typos-in-README.amd-maps.patch
Patch765: autofs-5.1.2-add-ref-counting-to-struct-map_source.patch
Patch766: autofs-5.1.2-add-support-for-amd-browsable-option.patch
Patch767: autofs-5.1.2-add-function-conf_amd_get_map_name.patch
Patch768: autofs-5.1.2-add-function-conf_amd_get_mount_paths.patch
Patch769: autofs-5.1.2-include-amd-mount-section-mounts-in-master-mounts-list.patch
Patch770: autofs-5.1.2-check-for-conflicting-amd-section-mounts.patch
Patch771: autofs-5.1.2-add-function-conf_amd_get_map_options.patch
Patch772: autofs-5.1.2-capture-cache-option-and-its-settings-during-parsing.patch
Patch773: autofs-5.1.2-handle-map_option-cache-for-top-level-mounts.patch
Patch774: autofs-5.1.2-handle-amd-cache-option-all-in-amd-type-auto-mounts.patch
Patch775: autofs-5.1.2-fix-bogus-check-in-expire_cleanup.patch
Patch776: autofs-5.1.2-delay-submount-exit-for-amd-submounts.patch

Patch777: autofs-5.1.2-add-the-mount-requestor-s-pid-to-pending_args.patch
Patch778: autofs-5.1.2-create-thread-local-ID-for-mount-attempts.patch
Patch779: autofs-5.1.2-log-functions-to-prefix-messages-with-attempt_id-if-available.patch
Patch780: autofs-5.1.2-factor-out-set-thread-mount-request-log-id.patch
Patch781: autofs-5.1.2-add-config-option-to-use-mount-request-log-id.patch

Patch782: autofs-5.1.2-work-around-sss-startup-delay.patch
Patch783: autofs-5.1.2-add-sss-master-map-wait-config-option.patch

Patch784: autofs-5.1.2-use-autofs_point-to-store-expire-timeout-where-possibe.patch
Patch785: autofs-5.1.2-fix-possible-NULL-derefernce.patch
Patch786: autofs-5.1.2-fix-work-around-sss-startup-delay.patch

Patch787: autofs-5.1.1-improve-scalability-of-direct-mount-path-component-creation.patch
Patch788: autofs-5.1.2-fix-invalid-reference-in-remount_active_mount.patch
Patch789: autofs-5.1.2-increase-worker-thread-per-thread-stack-size.patch
Patch790: autofs-5.1.2-limit-getgrgid_r-buffer-size.patch
Patch791: autofs-5.1.2-add-congigure-option-for-limiting-getgrgid_r-stack-usage.patch
Patch792: autofs-5.1.3-fix-unset-tsd-group-name-handling.patch

Patch793: autofs-5.1.3-set-systemd-KillMode-to-process.patch
Patch794: autofs-5.1.3-fix-mount_nfs-blocks-on-first-mount.patch
Patch795: autofs-5.1.3-fix-a-couple-of-typos-in-autofs-man-pages.patch
Patch796: autofs-5.1.3-fix-some-man-problems.patch
Patch797: autofs-5.1.3-allow-dot-in-OPTIONSTR-value-lexer-pattern.patch
Patch798: autofs-5.1.3-revert-fix-argc-off-by-one-in-mount_autofs_c.patch
Patch799: autofs-5.1.3-only-take-master-map-mutex-for-master-map-update.patch
Patch800: autofs-5.1.3-fix-nisplus-lookup-init-not-configured-check.patch
Patch801: autofs-5.1.3-make-open_lookup-error-handling-more-consistent.patch
Patch802: autofs-5.1.3-be-silent-about-sss-library-not-found.patch
Patch803: autofs-5.1.3-be-silent-about-nis-domain-not-set.patch
Patch804: autofs-5.1.3-make-map-source-reference-message-debug-only.patch
Patch805: autofs-5.1.3-handle-additional-nfs-versions-in-mount_nfs_c.patch
Patch806: autofs-5.1.3-improve-description-of-mount_nfs_default_protocol.patch
Patch807: autofs-5.1.3-reset-master-map-list-on-startup-retry.patch

# Bug 1509043
Patch810: autofs-5.1.3-improve-debug-logging-of-lookup-key.patch
Patch811: autofs-5.1.2-fix-cachefs-parse-message-not-being-logged.patch
Patch812: autofs-5.1.3-fix-typo-in-amd_parse_c.patch
Patch813: autofs-5.1.3-add-missing-MODPREFIX-to-logging-in-amd-parser.patch
Patch814: autofs-5.1.3-fix-symlink-false-negative-in-umount_multi.patch
Patch815: autofs-5.1.3-remove-expand_selectors-call-on-amd-parser-entry.patch
Patch816: autofs-5.1.3-fix-amd-defaults-map-entry-handling.patch
Patch817: autofs-5.1.3-refactor-amd_parse_c.patch
Patch818: autofs-5.1.3-fix-amd-parser-double-quote-handling.patch
Patch819: autofs-5.1.3-fix-expandamdent-quote-handling.patch
Patch820: autofs-5.1.3-fix-possible-memory-leak-during-amd-parse.patch
Patch821: autofs-5.1.3-remove-path-restriction-of-amd-external-mount.patch
Patch822: autofs-5.1.3-add-function-umount_amd_ext_mount.patch
Patch823: autofs-5.1.3-add-function-ext_mount_inuse.patch
Patch824: autofs-5.1.3-add-function-construct_argv.patch
Patch825: autofs-5.1.3-add-amd-mount-type-program-mount-support.patch
Patch826: autofs-5.1.3-fix-memory-leak-in-umount_amd_ext_mount.patch
Patch827: autofs-5.1.3-fix-strerror_r-parameter-declaration-in-do_program_mount.patch
Patch828: autofs-5.1.3-fix-incorrect-check-in-validate_program_options.patch

Patch829: autofs-5.1.3-update-configure-to-check-for-pipe2.patch
Patch830: autofs-5.1.3-fix-open-calls-not-using-open_xxxx-calls.patch
Patch831: autofs-5.1.3-move-open_xxxx-functions-to-spawn_c.patch
Patch832: autofs-5.1.3-serialize-calls-to-open_xxxx-functions.patch

Patch833: autofs-5.1.4-fix-use-after-free-in-do_master_list_reset.patch
Patch834: autofs-5.1.4-fix-deadlock-in-dumpmaps.patch

Patch835: autofs-5.1.4-dont-use-array-for-path-when-not-neccessary.patch
Patch836: autofs-5.1.4-fix-prefix-option-handling-in-expand_entry.patch
Patch837: autofs-5.1.4-fix-sublink-option-not-set-from-defaults.patch
Patch838: autofs-5.1.4-fix-error-return-in-do_nfs_mount.patch

Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%if %{with_systemd}
BuildRequires: systemd-units
%endif
BuildRequires: autoconf, hesiod-devel, openldap-devel, bison, flex, libxml2-devel, cyrus-sasl-devel, openssl-devel module-init-tools util-linux nfs-utils e2fsprogs libtirpc-devel
BuildRequires: libsss_autofs
Conflicts: cyrus-sasl-lib < 2.1.23-9
Requires: bash coreutils sed gawk textutils sh-utils grep module-init-tools /bin/ps
%if %{with_systemd}
Requires(post): systemd-sysv
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
%else
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/service
Requires(postun): /sbin/service
Requires(postun): /sbin/chkconfig
%endif
Summary(de): autofs daemon 
Summary(fr): démon autofs
Summary(tr): autofs sunucu süreci
Summary(sv): autofs-daemon

%description
autofs is a daemon which automatically mounts filesystems when you use
them, and unmounts them later when you are not using them.  This can
include network filesystems, CD-ROMs, floppies, and so forth.

%description -l de
autofs ist ein Dämon, der Dateisysteme automatisch montiert, wenn sie 
benutzt werden, und sie später bei Nichtbenutzung wieder demontiert. 
Dies kann Netz-Dateisysteme, CD-ROMs, Disketten und ähnliches einschließen. 

%description -l fr
autofs est un démon qui monte automatiquement les systèmes de fichiers
lorsqu'on les utilise et les démonte lorsqu'on ne les utilise plus. Cela
inclus les systèmes de fichiers réseau, les CD-ROMs, les disquettes, etc.

%description -l tr
autofs, kullanýlan dosya sistemlerini gerek olunca kendiliðinden baðlar
ve kullanýmlarý sona erince yine kendiliðinden çözer. Bu iþlem, að dosya
sistemleri, CD-ROM'lar ve disketler üzerinde yapýlabilir.

%description -l sv
autofs är en daemon som mountar filsystem när de använda, och senare
unmountar dem när de har varit oanvända en bestämd tid.  Detta kan
inkludera nätfilsystem, CD-ROM, floppydiskar, och så vidare.

%prep
%setup -q
echo %{version}-%{release} > .version
%if %{with_systemd}
  %define unitdir %{?_unitdir:/usr/lib/systemd/system}
  %define systemd_configure_arg --with-systemd
%endif
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%patch98 -p1
%patch99 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1

# pre-patches for amd parser series.
%patch400 -p1
%patch401 -p1
%patch402 -p1
%patch403 -p1
%patch404 -p1
%patch405 -p1
%patch406 -p1
%patch407 -p1
%patch408 -p1
%patch409 -p1
%patch410 -p1
%patch411 -p1
%patch412 -p1
%patch413 -p1
%patch414 -p1
%patch415 -p1
%patch416 -p1
%patch417 -p1
%patch418 -p1
%patch419 -p1
%patch420 -p1
%patch421 -p1
%patch422 -p1
%patch423 -p1
%patch424 -p1
%patch425 -p1
%patch426 -p1
%patch427 -p1
%patch428 -p1
%patch429 -p1
%patch430 -p1
%patch431 -p1
%patch432 -p1
%patch433 -p1
%patch434 -p1
%patch435 -p1

# amd parser series (set1)
%patch500 -p1
%patch501 -p1
%patch502 -p1
%patch503 -p1
%patch504 -p1
%patch505 -p1
%patch506 -p1
%patch507 -p1
%patch508 -p1
%patch509 -p1
%patch510 -p1
%patch511 -p1
%patch512 -p1
%patch513 -p1
%patch514 -p1
%patch515 -p1
%patch516 -p1
%patch517 -p1
%patch518 -p1
%patch519 -p1
%patch520 -p1
%patch521 -p1
%patch522 -p1
%patch523 -p1
%patch524 -p1
%patch525 -p1
%patch526 -p1
%patch527 -p1
%patch528 -p1
%patch529 -p1
%patch530 -p1
%patch531 -p1
%patch532 -p1
%patch533 -p1
%patch534 -p1
%patch535 -p1
%patch536 -p1
%patch537 -p1
%patch538 -p1
%patch539 -p1
%patch540 -p1
%patch541 -p1
%patch542 -p1
%patch543 -p1
%patch544 -p1
%patch545 -p1
%patch546 -p1
%patch547 -p1
%patch548 -p1
%patch549 -p1
%patch550 -p1
%patch551 -p1

# amd parser series (set2)
%patch552 -p1
%patch553 -p1
%patch554 -p1
%patch555 -p1
%patch556 -p1
%patch557 -p1
%patch558 -p1
%patch559 -p1
%patch560 -p1
%patch561 -p1
%patch562 -p1
%patch563 -p1
%patch564 -p1
%patch565 -p1
%patch566 -p1
%patch567 -p1
%patch568 -p1

%patch600 -p1
%patch601 -p1
%patch602 -p1
%patch603 -p1
%patch604 -p1
%patch605 -p1
%patch606 -p1
%patch607 -p1
%patch608 -p1
%patch609 -p1
%patch610 -p1
%patch611 -p1
%patch612 -p1
%patch613 -p1
%patch614 -p1
%patch615 -p1
%patch616 -p1
%patch617 -p1
%patch618 -p1
%patch619 -p1
%patch620 -p1
%patch621 -p1
%patch622 -p1
%patch623 -p1
%patch624 -p1
%patch625 -p1
%patch626 -p1
%patch627 -p1

%patch628 -p1
%patch629 -p1
%patch630 -p1
%patch631 -p1
%patch632 -p1
%patch633 -p1
%patch634 -p1
%patch635 -p1
%patch636 -p1
%patch637 -p1
%patch638 -p1
%patch639 -p1
%patch640 -p1
%patch641 -p1
%patch642 -p1

%patch643 -p1
%patch644 -p1
%patch645 -p1
%patch646 -p1
%patch647 -p1
%patch648 -p1
%patch649 -p1
%patch650 -p1
%patch651 -p1
%patch652 -p1
%patch653 -p1
%patch654 -p1
%patch655 -p1

%patch700 -p1
%patch701 -p1
%patch702 -p1
%patch703 -p1
%patch704 -p1

%patch705 -p1
%patch706 -p1
%patch707 -p1
%patch708 -p1

# Series 1 - additional bug fixes (bug 1300500)
%patch709 -p1
%patch710 -p1
%patch711 -p1
%patch712 -p1

# Series2 - add reinit method and change lookup to use reinit
# instead of reopen (bug 1300500)
%patch713 -p1
%patch714 -p1
%patch715 -p1
%patch716 -p1
%patch717 -p1
%patch718 -p1
%patch719 -p1
%patch720 -p1
%patch721 -p1
%patch722 -p1
%patch723 -p1
%patch724 -p1
%patch725 -p1
%patch726 -p1
%patch727 -p1
%patch728 -p1
%patch729 -p1
%patch730 -p1
%patch731 -p1
%patch732 -p1
%patch733 -p1

# Aditional bug fixes (bug 1300500)
%patch734 -p1
%patch735 -p1

# Some Coverity fixes identified for recent changes (bug 1300500)
%patch736 -p1
%patch737 -p1
%patch738 -p1
%patch739 -p1
%patch740 -p1

%patch741 -p1
%patch742 -p1
%patch743 -p1

%patch744 -p1
%patch745 -p1
%patch746 -p1
%patch747 -p1
%patch748 -p1
%patch749 -p1
%patch750 -p1

%patch751 -p1
%patch752 -p1
%patch753 -p1
%patch754 -p1
%patch755 -p1

# Bug 1367576
%patch760 -p1
%patch761 -p1
%patch762 -p1
%patch763 -p1
%patch764 -p1
%patch765 -p1
%patch766 -p1
%patch767 -p1
%patch768 -p1
%patch769 -p1
%patch770 -p1
%patch771 -p1
%patch772 -p1
%patch773 -p1
%patch774 -p1
%patch775 -p1
%patch776 -p1

%patch777 -p1
%patch778 -p1
%patch779 -p1
%patch780 -p1
%patch781 -p1

%patch782 -p1
%patch783 -p1

%patch784 -p1
%patch785 -p1
%patch786 -p1

%patch787 -p1
%patch788 -p1
%patch789 -p1
%patch790 -p1
%patch791 -p1
%patch792 -p1

%patch793 -p1
%patch794 -p1
%patch795 -p1
%patch796 -p1
%patch797 -p1
%patch798 -p1
%patch799 -p1
%patch800 -p1
%patch801 -p1
%patch802 -p1
%patch803 -p1
%patch804 -p1
%patch805 -p1
%patch806 -p1
%patch807 -p1

# Bug 1509043
%patch810 -p1
%patch811 -p1
%patch812 -p1
%patch813 -p1
%patch814 -p1
%patch815 -p1
%patch816 -p1
%patch817 -p1
%patch818 -p1
%patch819 -p1
%patch820 -p1
%patch821 -p1
%patch822 -p1
%patch823 -p1
%patch824 -p1
%patch825 -p1
%patch826 -p1
%patch827 -p1
%patch828 -p1

%patch829 -p1
%patch830 -p1
%patch831 -p1
%patch832 -p1

%patch833 -p1
%patch834 -p1

%patch835 -p1
%patch836 -p1
%patch837 -p1
%patch838 -p1

%build
LDFLAGS=-Wl,-z,now
%configure --disable-mount-locking \
	   --enable-ignore-busy \
	   --with-libtirpc \
	   --enable-limit-getgrgid-size \
	   %{?systemd_configure_arg:}
make initdir=%{_initrddir} DONTSTRIP=1

%install
rm -rf $RPM_BUILD_ROOT
%if %{with_systemd}
install -d -m 755 $RPM_BUILD_ROOT%{unitdir}
%else
mkdir -p -m755 $RPM_BUILD_ROOT%{_initrddir}
%endif
mkdir -p -m755 $RPM_BUILD_ROOT%{_sbindir}
mkdir -p -m755 $RPM_BUILD_ROOT%{_libdir}/autofs
mkdir -p -m755 $RPM_BUILD_ROOT%{_mandir}/{man5,man8}
mkdir -p -m755 $RPM_BUILD_ROOT/etc/sysconfig
mkdir -p -m755 $RPM_BUILD_ROOT/etc/auto.master.d

make install mandir=%{_mandir} initdir=%{_initrddir} systemddir=%{unitdir} INSTALLROOT=$RPM_BUILD_ROOT
echo make -C redhat
make -C redhat
install -m 755 -d $RPM_BUILD_ROOT/misc
%if %{with_systemd}
# Configure can get this wrong when the unit files appear under /lib and /usr/lib
find $RPM_BUILD_ROOT -type f -name autofs.service -exec rm -f {} \;
install -m 644 redhat/autofs.service $RPM_BUILD_ROOT%{unitdir}/autofs.service
%define init_file_name %{unitdir}/autofs.service
%else
install -m 755 redhat/autofs.init $RPM_BUILD_ROOT%{_initrddir}/autofs
%define init_file_name /etc/rc.d/init.d/autofs
%endif
install -m 644 redhat/autofs.conf $RPM_BUILD_ROOT/etc/autofs.conf
install -m 644 redhat/autofs.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/autofs

%clean
rm -rf $RPM_BUILD_ROOT

%post
%if %{with_systemd}
%systemd_post %{name}.service
%else
if [ $1 -eq 1 ]; then
	%{_sbindir}/sbin/chkconfig --add autofs
fi
%endif

%preun
%if %{with_systemd}
%systemd_preun %{name}.service
%else
if [ $1 -eq 0 ] ; then
    %{_sbindir}/service autofs stop > /dev/null 2>&1 || :
    %{_sbindir}/chkconfig --del autofs
fi
%endif

%postun
%if %{with_systemd}
%systemd_postun_with_restart %{name}.service
%else
if [ $1 -ge 1 ] ; then
    %{_sbindir}/sbin/service autofs condrestart > /dev/null 2>&1 || :
fi
%endif

%triggerun -- %{name} < 5.0.6-5
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply %{name}
# to migrate them to systemd targets
%{_bindir}/systemd-sysv-convert --save %{name} >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
%{_sbindir}/chkconfig --del %{name} >/dev/null 2>&1 || :
%{_bindir}/systemctl try-restart %{name}.service >/dev/null 2>&1 || :

%files
%defattr(-,root,root,-)
%doc CREDITS INSTALL COPY* README* patches/* samples/ldap* samples/autofs.schema samples/autofs.schema.new
%config %{init_file_name}
%config(noreplace,missingok) /etc/auto.master
%config(noreplace,missingok) /etc/auto.misc
%config(noreplace,missingok) /etc/auto.net
%config(noreplace,missingok) /etc/auto.smb
%config(noreplace) /etc/autofs.conf
%config(noreplace) /etc/sysconfig/autofs
%config(noreplace) /etc/autofs_ldap_auth.conf
%{_sbindir}/automount
%{_mandir}/*/*
%{_libdir}/autofs/
%dir /etc/auto.master.d

%changelog
* Fri Feb 02 2018 Ian Kent <ikent@redhat.com> - 5.0.7-83
- bz1509043 - [RFE] "automount / amd: file system type program is not
  yet implemented"
  - dont use array for path when not necessary.
  - fix prefix option handling in expand_entry().
  - fix sublink handling in do_nfs_mount().
  - add fix error return in do_nfs_mount().
- Related: rhbz#1509043

* Fri Dec 22 2017 Ian Kent <ikent@redhat.com> - 5.0.7-82
- bz1527815 - automount[1979]: segfault at 55f5101d30e8 ip 000055f50f177668
              sp 00007ffffa85fdd0 error 4 in automount[55f50f16d000+48000]
  - fix deadlock in dumpmaps.
- Related: rhbz#1527815

* Thu Dec 21 2017 Ian Kent <ikent@redhat.com> - 5.0.7-81
- bz1527815 - automount[1979]: segfault at 55f5101d30e8 ip 000055f50f177668
              sp 00007ffffa85fdd0 error 4 in automount[55f50f16d000+48000]
  - fix use after free in do_master_list_reset()
- Resolves: rhbz#1527815

* Mon Dec 18 2017 Ian Kent <ikent@redhat.com> - 5.0.7-80
- bz1509088 - autofs hangs due to race condition in do_spawn
  - update configure to check for pipe2(2).
  - fix open calls not using open_xxxx() calls.
  - move open_xxxx() functions to spawn.c.
  - serialize calls to open_xxxx() functions.
- Resolves: rhbz#1509088

* Mon Dec 11 2017 Ian Kent <ikent@redhat.com> - 5.0.7-79
- bz1509043 - [RFE] "automount / amd: file system type program is not
  yet implemented"
  - fix memory leak in umount_amd_ext_mount().
  - fix strerror_r() parameter declaration in do program_mount().
  - fix incorrect check in validate_program_options().
- Related: rhbz#1509043

* Mon Dec 11 2017 Ian Kent <ikent@redhat.com> - 5.0.7-78
- bz1509043 - [RFE] "automount / amd: file system type program is not
  yet implemented"
  - improve debug logging of lookup key.
  - fix cachefs parse message not being logged.
  - fix typo in amd_parse.c.
  - add missing MODPREFIX to logging in amd parser.
  - fix symlink false negative in umount_multi().
  - remove expand_selectors() call on amd parser entry.
  - fix amd defaults map entry handling.
  - refactor amd_parse.c.
  - fix amd parser double quote handling.
  - fix expandamdent() quote handling.
  - fix possible memory leak during amd parse.
  - remove path restriction of amd external mount.
  - add function umount_amd_ext_mount().
  - add function ext_mount_inuse().
  - add function construct_argv().
  - add amd mount type program mount support.
- Resolves: rhbz#1509043

* Tue Oct 31 2017 Ian Kent <ikent@redhat.com> - 5.0.7-77
- bz1504145 - Automount cannot access host shares after a reboot
  - fix reject in patch changelog hunk.
- Related: rhbz#1504145

* Tue Oct 31 2017 Ian Kent <ikent@redhat.com> - 5.0.7-76
- bz1504145 - Automount cannot access host shares after a reboot
  - reset master map list on startup retry.
- Resolves: rhbz#1504145

* Fri Oct 27 2017 Ian Kent <ikent@redhat.com> - 5.0.7-75
- bz1489247 - autofs: config mount_nfs_default_protocol doesn't work
  - improve description of mount_nfs_default_protocol.
- Resolves: rhbz#1489247

* Thu Oct 19 2017 Ian Kent <ikent@redhat.com> - 5.0.7-74
- bz1486035 - autofs map entry options field does not accept dot character
  - handle additional nfs versions in mount_nfs.c.
- Related: rhbz#1486035

* Wed Oct 11 2017 Ian Kent <ikent@redhat.com> - 5.0.7-73
- bz1489648 - autofs missing dependency with libsss_autofs cause missing file
  messages during boot
  - fix nisplus lookup init not configured check.
  - make open_lookup() error handling more consistent.
  - be silent about sss library not found.
  - be silent about nis domain not set.
  - make map source reference message debug only.
- Resolves: rhbz#1489648

* Mon Oct 9 2017 Ian Kent <ikent@redhat.com> - 5.0.7-72
- bz1499287 - Autofs processes hung while waiting for the release of an entry
  master_lock that is held by another thread waiting on a bind mount
  - only take master map mutex for master map update.
- Resolves: rhbz#1499287

* Thu Oct 5 2017 Ian Kent <ikent@redhat.com> - 5.0.7-71
- bz1497846 - Macro definitions specified in mount entries are no longer getting set
  - revert fix argc off by one in mount_autofs.c.
- Resolves: rhbz#1497846

* Mon Oct 2 2017 Ian Kent <ikent@redhat.com> - 5.0.7-70
- bz1442926 - Systemd kills autofs fuse mount on service restart
  - set systemd KillMode to process.
- bz1466256 - autofs: unable to mount nfs share after reboot
  - fix mount.nfs blocks on first mount.
- bz1476850 - Man page: Make auto.master 's summary findable via 'man -k autofs'
  - fix typos in autofs man pages.
  - fix some man page problems.
- bz1486035 - autofs map entry options field does not accept dot character
  - allow dot in OPTIONSTR value lexer pattern.
-Resolves: rhbz#1442926 rhbz#1466256 rhbz#1476850 rhbz#1486035

* Fri Jun 2 2017 Ian Kent <ikent@redhat.com> - 5.0.7-69
- bz1435736 - autofs fails with kernel: automount[3386]:
    segfault at 7f3fb7595ca8 ip 00007f3fb61e353a sp 00007f3fb7595cb0
    error 6 in libc-2.17.so[7f3fb60b7000+1b6000]
  - fix a couple of covarity warning resulting in group name handling change.
- Related: rhbz#1435736

* Fri Jun 2 2017 Ian Kent <ikent@redhat.com> - 5.0.7-68
- bz1435736 - autofs fails with kernel: automount[3386]:
    segfault at 7f3fb7595ca8 ip 00007f3fb61e353a sp 00007f3fb7595cb0
    error 6 in libc-2.17.so[7f3fb60b7000+1b6000]
  - fix unset tsd group name handling.
- Related: rhbz#1435736

* Fri May 05 2017 Ian Kent <ikent@redhat.com> - 5.0.7-66
- bz1435736 - autofs fails with kernel: automount[3386]:
    segfault at 7f3fb7595ca8 ip 00007f3fb61e353a sp 00007f3fb7595cb0
    error 6 in libc-2.17.so[7f3fb60b7000+1b6000]
  - increase worker thread per-thread stack size.
  - limit getgrgid_r() buffer size.
  - add congigure option for limiting getgrgid_r() stack usage.
  - use above option to limit getgrgid_r() stack usage with configure.
- Resolves: rhbz#1435736

* Mon Apr 24 2017 Ian Kent <ikent@redhat.com> - 5.0.7-65
- bz1367576 - [RFE] Add browsing support into autofs for AMD format maps
  - fix invalid reference in remount_active_mount().
- Related: rhbz#1367576

* Mon Apr 17 2017 Ian Kent <ikent@redhat.com> - 5.0.7-64
- bz1440769 - autofs is facing scalability issues
  - improve scalability of direct mount path component creation.
- Resolves: rhbz#1440769

* Thu Mar 30 2017 Ian Kent <ikent@redhat.com> - 5.0.7-63
- bz1101782 - autofs configured with sssd is not finding any maps
  - fix work around sss startup delay.
- bz1367576 - [RFE] Add browsing support into autofs for AMD format maps
  - fix possible NULL derefernce.
- Related: rhbz#1101782 rhbz#1367576

* Mon Mar 27 2017 Ian Kent <ikent@redhat.com> - 5.0.7-62
- bz1367576 - [RFE] Add browsing support into autofs for AMD format maps
  - use autofs_point to store expire timeout where possibe.
- Related: rhbz#1367576

* Mon Mar 20 2017 Ian Kent <ikent@redhat.com> - 5.0.7-61
- bz1101782 - autofs configured with sssd is not finding any maps
  - work around sss startup delay.
  - add sss master map wait config option (wait initially 0, disabled).
- Resolves: rhbz#1101782

* Mon Mar 20 2017 Ian Kent <ikent@redhat.com> - 5.0.7-60
 - bz1382093 - Improve logging in autofs
   - add the mount requestor's pid to pending_args.
   - create thread-local ID for mount attempts.
   - log functions to prefix messages with attempt_id if available.
   - factor out set_thread_mount_request_log_id().
   - add config option to use mount request log id.
- Resolves: rhbz#1382093

* Wed Mar 15 2017 Ian Kent <ikent@redhat.com> - 5.0.7-59
- bz1383910 - Incorrect autofs.schema
  - update and add README for old autofs schema
- bz1367576 - [RFE] Add browsing support into autofs for AMD format maps
  - fix short memory allocation in lookup_amd_instance().
  - fix count_mounts() function.
  - fix argc off by one in mount_autofs.c.
  - fix _strncmp() usage.
  - fix typos in README.amd-maps.
  - add ref counting to struct map_source.
  - add support for amd browsable option.
  - add function conf_amd_get_map_name().
  - add function conf_amd_get_mount_paths().
  - include amd mount section mounts in master mounts list.
  - check for conflicting amd section mounts.
  - add function conf_amd_get_map_options().
  - capture cache option and its settings during parsing.
  - handle map_option cache for top level mounts.
  - handle amd cache option all in amd type auto mounts.
  - fix bogus check in expire_cleanup().
  - delay submount exit for amd submounts.
- Resolves: rhbz#1383910 rhbz#1367576

* Wed Mar 01 2017 Ian Kent <ikent@redhat.com> - 5.0.7-58
- bz1420584 - RHEL7.3: shutdown / reboot hangs with findmnt in a readlink
  system call, doing path_walk and stuck in autofs4_wait
  - make set_direct_mount_catatonic() more general.
  - set autofs mounts catatonic at exit.
- bz1396403 - Trying to access a non-existent directory using automount
  results in 4 minute hang as not checking the local mount availability
  - check NFS server availability on local mount fallback.
- bz1399796 - local nfs share being bind-mounted by autofs is mounted
  read-only even when marked rw in its map
  - honor last rw in mount options when doing a bind mount.
- Resolves: rhbz#1420584 rhbz#1396403 rhbz#1399796

* Sat Feb 04 2017 Ian Kent <ikent@redhat.com> - 5.0.7-57
- bz1383194 - On every system boot automount needs a restart to access
  NIS map
  - wait for master map available at start.
  - add master read wait option.
  - fix included master map not found return.
  - dont exit on master map read fail timeout.
  - set sane default master read wait timeout.
  - don't return until after master map retry read.
  - make lookup_nss_read_master() return nss status.
- Resolves: rhbz#1383194

* Wed May 25 2016 Ian Kent <ikent@redhat.com> - 1:5.0.7-56
- bz1327388 - Fix use-after-free in st_queue_handler
  - fix use-after-free in st_queue_handler().
- bz1252071 - [RFE] Disable alerting on non-existent automounts
  - add config option to suppress not found log message.
- Resolves: rhbz#1327388 rhbz#1252071

* Tue May 17 2016 Ian Kent <ikent@redhat.com> - 1:5.0.7-55
- bz1298115 - The autofs service fails to load maps on boot if the maps
  are stored on a NFS mount
  - make service want network-online.
  - add remote-fs.target systemd dependency.
- bz1300496 - Duplicate mounts created or leftovers in mtab
  - revert special case cifs escapes.
- bz1300498 - Parent directory in nested mount gets unmounted while the
  child remains mounted
  - guard against incorrect umount return.
- bz1305721 - autofs.conf: Fix 'nameing' typo
  - fix 'nameing' typo in autofs.conf.
- bz1329869 - RHEL6.7: shutdown / reboot hangs with findmnt in a readlink
  system call, doing path_walk and stuck in autofs4_wait
  - always set direct mounts catatonic at exit.
  - log pipe read errors.
  - fix rwlock unlock crash.
  - fix handle_mounts() termination condition check.
- bz1300500 - double free or corruption (fasttop) causes abort in
  ldap_int_tls_destroy
  - fix config old name lookup.
  - fix error handling on ldap bind fail.
  - fix gcc5 complaints.
  - fix fix gcc5 complaints.
  - fix missing source sss in multi map lookup.
  - fix update_hosts_mounts() return.
  - change lookup to use reinit instead of reopen.
  - fix unbind sasl external mech.
  - fix sasl connection concurrancy problem.
  - add some Coverity fixes identified for recent changes.
- bz1300501 - Request to add a configuration option to force use of the map
  entry hostname for mounts
  - add configuration option to use fqdn in mounts
- Resolves: rhbz#1298115 rhbz#1300496 rhbz#1300498 rhbz#1305721
- Resolves: rhbz#1329869 rhbz#1300500 rhbz#1300501

* Thu Sep 17 2015 Ian Kent <ikent@redhat.com> - 1:5.0.7-54
- bz1263508 - Heavy program map usage can lead to a hang
  - fix out of order call in program map lookup.
- Resolves: rhbz#1263508

* Tue Jul 7  2015 Ian Kent <ikent@redhat.com> - 1:5.0.7-53
- bz1238573 - RFE: autofs MAP_HASH_TABLE_SIZE description
  - update map_hash_table_size description.
- Resolves: rhbz#1238573

* Thu Jul 2  2015 Ian Kent <ikent@redhat.com> - 1:5.0.7-52
- bz1233069 - Direct map does not expire if map is initially empty
  - update patch to fix expiry problem.
- Related: rhbz#1233069

* Tue Jun 23 2015 Ian Kent <ikent@redhat.com> - 1:5.0.7-51
- bz1233065 - 'service autofs reload' does not reloads new mounts only
  when 'sss' or 'ldap' is used in '/etc/nsswitch.conf' file
  - init qdn before use in get_query_dn().
  - fix left mount count return from umount_multi_triggers().
  - fix return handling in sss lookup module.
  - move query dn calculation from do_bind() to do_connect().
  - make do_connect() return a status.
  - make connect_to_server() return a status.
  - make find_dc_server() return a status.
  - make find_server() return a status.
  - fix return handling of do_reconnect() in ldap module.
- bz1233067 - autofs is performing excessive direct mount map re-reads
  - fix direct mount stale instance flag reset.
- bz1233069 - Direct map does not expire if map is initially empty
  - fix direct map expire not set for initial empty map.
- Resolves: rhbz#1233065 rhbz#1233067 rhbz#1233069

* Tue May 26 2015 Ian Kent <ikent@redhat.com> - 1:5.0.7-50
- bz1218045 - Similar but unrelated NFS exports block proper mounting of
  "parent" mount point
  - remove unused offset handling code.
  - fix mount as you go offset selection.
- Resolves: rhbz#1218045

* Mon May 25 2015 Ian Kent <ikent@redhat.com> - 1:5.0.7-49
- bz1166457 - Autofs unable to mount indirect after attempt to mount wildcard
  - make negative cache update consistent for all lookup modules.
  - ensure negative cache isn't updated on remount.
  - dont add wildcard to negative cache.
- bz1162041 - priv escalation via interpreter load path for program based
  automount maps
  - add a prefix to program map stdvars.
  - add config option to force use of program map stdvars.
- bz1161474 - automount segment fault in parse_sun.so for negative parser tests
  - fix incorrect check in parse_mount().
- bz1205600 - Autofs stopped mounting /net/hostname/mounts after seeing duplicate
  exports in the NFS server
  - handle duplicates in multi mounts.
- bz1201582 - autofs: MAPFMT_DEFAULT is not macro in lookup_program.c
  - fix macro usage in lookup_program.c.
- Resolves: rhbz#1166457 rhbz#1162041 rhbz#1161474 rhbz#1205600 rhbz#1201582

* Fri Dec 19 2014 Ian Kent <ikent@redhat.com> - 1:5.0.7-48
- bz1164957 - The default installed autofs.conf doesn't have default nfs
  protocol set to 4
  - add missing line to copy RedHat customized config to spec file.
- Resolves: rhbz#1164957

* Tue Oct 28 2014 Ian Kent <ikent@redhat.com> - 1:5.0.7-47
- bz1156662 - autofs /net maps do not refresh list of shares exported on
  the NFS server
  - fix typo in update_hosts_mounts().
  - fix hosts map update on reload.
- Resolves: rhbz#1156662

* Fri Oct 17 2014 Ian Kent <ikent@redhat.com> - 1:5.0.7-46
- bz1153414 - autofs-5.0.5-109 with upgrade to RHEL 6.6 no longer recognizes
  +yp: in auto.master
  - fix fix master map type check.
- Resolves: rhbz#1153414

* Wed Oct 15 2014 Ian Kent <ikent@redhat.com> - 1:5.0.7-45
- bz1152862 - autofs shouldn't have kernel as a dependency
  - remove an ancient kernel Requires.
- Resolves: rhbz#1152862

* Tue Oct 7 2014 Ian Kent <ikent@redhat.com> - 1:5.0.7-44
- bz1099800 - man page of /etc/init.d/autofs: /usr/share/man/man8/autofs.8.gz
  is not needed in RHEL-7
  - update man page autofs(8) for systemd
- Resolves: rhbz#1099800

* Thu Sep 25 2014 Ian Kent <ikent@redhat.com> - 1:5.0.7-43
- bz1066772 - Clarify autofs(5) man page sections "Multiple Mounts" and
  "Replicated Server"
  - clarify multiple mounts description.
- Resolves: rhbz#1066772

* Mon Sep 22 2014 Ian Kent <ikent@redhat.com> - 1:5.0.7-42
- bz1116184 - RFE: RHEL7: Add am-utils RPM or equivalent am-utils functionality
  to other packages
  - add amd map format parser.
- bz1132236 - Memory leak in get_exports
  - fix memory leak in create_client().
  - fix memory leak in get_exports().
- bz1135158 - double free or corruption (fasttop) causes abort in ldap_int_tls_destroy
  - fix deadlock in init_ldap_connection().
  - extend libldap serialization.
- Resolves: rhbz#1116184 rhbz#1132236 rhbz#1135158

* Mon Aug 25 2014 Ian Kent <ikent@redhat.com> - 1:5.0.7-41
- bz1094661 - autofs can ghost non-existent map entries given the right timing
  - fix negative status being reset on map read.
  - fix fix negative status being reset on map read.
  - check for non existent negative entries in lookup_ghost().
- bz1124389 - autofs-5.0.5-88.el6 breaks maps that have a -v in the options
  - allow use of hosts map in maps (dependent patch).
  - fix options compare.
  - fix fix options compare.
- Resolves: rhbz#1094661 rhbz#1124389

* Wed Feb 19 2014 Ian Kent <ikent@redhat.com> - 1:5.0.7-40
- bz1063139 - autofs regression test failure.
  - fix fix ipv6 libtirpc getport.
  - get_nfs_info() should query portmapper if port is not given.
  - fix rpc_portmap_getport() proto not set.
  - fix portmap not trying proto v2.
- Resolves: rhbz#1063139

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1:5.0.7-39
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1:5.0.7-38
- Mass rebuild 2013-12-27

* Sat Nov 30 2013 Ian Kent <ikent@redhat.com> - 1:5.0.7-37
- bz1035977 - with IPv6 address automount fail with "hostname lookup failed"
  - fix ipv6 link local address handling.
- Resolves: rhbz#1035977

* Tue Nov 19 2013 Ian Kent <ikent@redhat.com> - 1:5.0.7-35
- bz1030705 - Default unmount is in 10 seconds, man page says 10 minutes
  - improve timeout option description.
- Related: rhbz#1030705

* Tue Nov 19 2013 Ian Kent <ikent@redhat.com> - 1:5.0.7-35
- bz1029611 - Fresh rhel7 install can't automount nfs exports
  - fix ipv6 libtirpc getport function.
- Related: rhbz#1029611

* Thu Nov 14 2013 Ian Kent <ikent@redhat.com> - 1:5.0.7-34
- bz1029611 - Fresh rhel7 install can't automount nfs exports
  - fix revision in spec file.
- Resolves: rhbz#1029611

* Thu Nov 14 2013 Ian Kent <ikent@redhat.com> - 1:5.0.7-33
- bz1029611 - Fresh rhel7 install can't automount nfs exports
  - regenerate configure due to missing function.
- Resolves: rhbz#1029611

* Thu Nov 7 2013 Ian Kent <ikent@redhat.com> - 1:5.0.7-32
- bz1011909 - NFSv4 UDP packet sent during automounting
  - only probe specific nfs version if requested.
- Related: rhbz#1011909

* Tue Oct 22 2013 Ian Kent <ikent@redhat.com> - 1:5.0.7-31
- bz1011909 - NFSv4 UDP packet sent during automounting
  - fix get_nfs_info() probe.
  - fix portmap lookup.
- bz995979 - RFE: feature to dump automount maps in native file format
  - update dumpmaps patch with latest changes from QE testing.
- Resolves: rhbz#1011909 rhbz#995979

* Thu Aug 22 2013 Ian Kent <ikent@redhat.com> - 1:5.0.7-30
- bz852327 - RFE: feature to dump automount maps in native file format
  - fix dumpmaps multi output.
  - try and cleanup after dumpmaps.
  - teach dumpmaps to output simple key value pairs.
- Resolves: rhbz#852327

* Tue Aug 13 2013 Ian Kent <ikent@redhat.com> - 1:5.0.7-29
- bz994352 - "autofs reload" causes automount to stop running when multiple
  maps are removed from auto.master
  - fix syncronize handle_mounts() shutdown.
- bz994359 - Wildcard in nested mounts regression
  - fix fix wildcard multi map regression.
- Resolves: rhbz#994352 rhbz#994359

* Sat Jul 13 2013 Ian Kent <ikent@redhat.com> - 1:5.0.7-28
- bz983160 Package autofs-5.0.7-22.el7 failed RHEL7 RPMdiff testing
  - fix add null check in parse_server_string() (bz979155).
  - check for protocol option.
  - use ulimit max open files if greater than internal maximum.
  - fix default path used for unitdir.
  - fix changelog inconsistent dates.
  - fix default path used for unitdir.
  - fix changelog inconsistent dates.
  - link with full reloc options.
  - fix a couple of compiler warnings.
  - add after sssd dependency to unit file (bz984089).
- Resolves: rhbz#983160
+
* Wed Jun 19 2013 Ian Kent <ikent@redhat.com> - 1:5.0.7-22
- misc man page fixes (bz948517).

* Wed Jun 12 2013 Ian Kent <ikent@redhat.com> - 1:5.0.7-21
- fix probe each nfs version in turn for singleton mounts (bz973537).

* Tue Jun 11 2013 Ian Kent <ikent@redhat.com> - 1:5.0.7-20
- fix master map mount options matching.
- fix master map bogus keywork match.
- fix fix map entry duplicate offset detection.
- add a number of fixes based on a Covarity report.

* Mon May 27 2013 Ian Kent <ikent@redhat.com> - 1:5.0.7-19
- dont probe rdma mounts.

* Fri May 24 2013 Ian Kent <ikent@redhat.com> - 1:5.0.7-17
- fix interface address null check.

* Mon May 13 2013 Ian Kent <ikent@redhat.com> - 1:5.0.7-16
- make dump maps check for duplicate indirect mounts (bz961312).
- document allowed map sources in auto.master(5) (bz961312).
- add enable sloppy mount option to configure.

* Sun Apr 28 2013 Ian Kent <kent@redhat.com> - 1:5.0.7-14
- fix some automount(8) typos (bz664178).
- fix syncronize of handle_mounts() shutdown.
- fix submount tree not all expiring.

* Tue Mar 12 2013 Ian Kent <ikent@redhat.com> - 1:5.0.7-12
- dont fail on master map self include.
- fix wildcard multi map regression.
- fix file descriptor leak when reloading the daemon.
- depricate nosymlink pseudo option.
- add symlink pseudo option.
- update kernel include files.
- fix requires in spec file.
- fix libtirpc build option.
- fix systemd unidir in spec file.
- document browse option in man page.
- fix automounter support on parisc.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Ian Kent <ikent@redhat.com> - 1:5.0.7-10
- fix submount offset delete.
- fix init script status return.
- fix use get_proximity() without libtirpc.
- don't use dirent d_type to filter out files in scandir().
- don't schedule new alarms after readmap.
- use numeric protocol ids instead of protoent structs.
- lib/defaults.c: use WITH_LDAP conditional around LDAP types.
- make yellow pages support optional.
- modules/replicated.c: use sin6_addr.s6_addr32.
- workaround missing GNU versionsort extension.

* Tue Nov 20 2012 Ian Kent <ikent@redhat.com> - 1:5.0.7-9
- fix nobind man page description.

* Tue Nov 20 2012 Ian Kent <ikent@redhat.com> - 1:5.0.7-8
- fix map entry duplicate offset detection.
- Allow nsswitch.conf to not contain "automount:" lines.

* Thu Oct 18 2012 Ian Kent <ikent@redhat.com> - 1:5.0.7-7
- use spec file systemd unit file location.

* Thu Oct 18 2012 Ian Kent <ikent@redhat.com> - 1:5.0.7-6
- fix recursive mount deadlock.
- increase file map read buffer size.
- handle new location of systemd.

* Tue Oct 16 2012 Ian Kent <ikent@redhat.com> - 1:5.0.7-5
- configure: allow cross compilation update.
- fix date in changelog entry.

* Mon Oct 15 2012 Ian Kent <ikent@redhat.com> - 1:5.0.7-4
- include usage in usage message.
- dont wait forever to restart.
- add option description to man page.
- fix null map entry order handling.
- make description of default MOUNT_WAIT setting clear.
- configure.in: allow cross compilation.
- README: update mailing list subscription info.
- allow non root user to check status.

* Mon Sep 10 2012 Ian Kent <ikent@redhat.com> - 1:5.0.7-3
- fix nobind sun escaped map entries.
- fix use cache entry after free mistake.
- fix ipv6 proximity calculation.
- fix parse buffer initialization.
- fix typo in automount(8).

* Mon Aug 27 2012 Ian Kent <ikent@redhat.com> - 1:5.0.7-2
- update systemd scriplet macros (bz850040).

* Wed Jul 25 2012 Ian Kent <ikent@redhat.com> - 1:5.0.7-1
- Update to upstream version 5.0.7.

* Wed Jul 25 2012 Ian Kent <ikent@redhat.com> - 1:5.0.6-24
- fix changelog message commit dates.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.0.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Ian Kent <ikent@redhat.com> - 1:5.0.6-21
- fix systemd argument passing.
- fix get_nfs_info() can incorrectly fail.
- fix offset directory removal.

* Tue Jul 3 2012 Ian Kent <ikent@redhat.com> - 1:5.0.6-21
- fix fix LDAP result leaks on error paths.
- report map not read when debug logging.
- duplicate parent options for included maps.
- update ->timeout() function to not return timeout.
- move timeout to map_source.
- fix kernel verion check of version components.
- dont retry ldap connect if not required.
- check if /etc/mtab is a link to /proc/self/mounts.
- fix nfs4 contacts portmap.
- make autofs wait longer for shutdown.
- fix sss map age not updated.
- fix remount deadlock.
- fix umount recovery of busy direct mount.
- fix offset mount point directory removal.
- remove move mount code and configure option.
- fix remount of multi mount.
- fix devce ioctl alloc path check.
- refactor hosts lookup module.
- remove cache update from parse_mount().
- add function to delete offset cache entry.
- allow update of multi mount offset entries.
- add hup signal handling to hosts map.

* Tue May 22 2012 Ian Kent <ikent@redhat.com> - 1:5.0.6-19
- fix libtirpc name clash (bz821847).

* Tue May 22 2012 Ian Kent <ikent@redhat.com> - 1:5.0.6-18
- update patch fix initialization in rpc create_client() (bz821847).

* Wed May 16 2012 Ian Kent <ikent@redhat.com> - 1:5.0.6-17
- fix initialization in rpc create_client() (bz821847).

* Tue May 1 2012 Ian Kent <ikent@redhat.com> - 1:5.0.6-16
- add libsss_autofs as a build dependency.

* Tue May 1 2012 Ian Kent <ikent@redhat.com> - 1:5.0.6-15
- fix typo in libtirpc file name.
- fix rework error return handling in rpc code.
- allow MOUNT_WAIT to override probe.
- improve UDP RPC timeout handling.
- fix segfault in get_query_dn().
- use strtok_r() in linux_version_code().
- fix sss wildcard match.
- fix dlopen() error handling in sss module.
- fix configure string length tests for sss library.

* Wed Feb 29 2012 Ian Kent <ikent@redhat.com> - 1:5.0.6-14
- fix function to check mount.nfs version.

* Sun Feb 26 2012 Ian Kent <ikent@redhat.com> - 1:5.0.6-13
- fix error in %post scriplet.

* Fri Feb 24 2012 Ian Kent <ikent@redhat.com> - 1:5.0.6-12
- ignore duplicate exports in auto.net.
- add kernel verion check function.
- add function to check mount.nfs version.
- reinstate singleton mount probe.
- rework error return handling in rpc code.
- catch EHOSTUNREACH and bail out early.
- systemd support fixes.
- fix segmentation fault in do_remount_indirect().

* Thu Feb 9 2012 Ian Kent <ikent@redhat.com> - 1:5.0.6-11
- fix fuzz in CHANGELOG hunk when applying patch26.

* Tue Feb 7 2012 Ian Kent <ikent@redhat.com> - 1:5.0.6-10
- fix rpc build error.
- add sss lookup module.
- teach automount about sss source.

* Mon Jan 23 2012 Ian Kent <ikent@redhat.com> - 1:5.0.6-9
- add correct patch for "fix improve mount location error reporting".
- add correct patch for "fix fix wait for master source mutex".

* Mon Jan 23 2012 Ian Kent <ikent@redhat.com> - 1:5.0.6-8
- fix fix wait for master source mutex.
- fix improve mount location error reporting (bz783496).

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 9 2011 Ian Kent <ikent@redhat.com> - 1:5.0.6-6
- remove empty command line arguments (passed by systemd).

* Mon Dec 5 2011 Ian Kent <ikent@redhat.com> - 1:5.0.6-5
- fix ipv6 name lookup check.
- fix ipv6 rpc calls.
- fix ipv6 configure check.
- add piddir to configure.
- add systemd unit support.
- fix MNT_DETACH define.

* Mon Dec 5 2011 Ian Kent <ikent@redhat.com> - 1:5.0.6-4
- fix lsb service name in init script 2 (bz712504).

* Tue Nov 8 2011 Ian Kent <ikent@redhat.com> - 1:5.0.6-3
- improve mount location error reporting.
- fix paged query more results check.
- fix dumpmaps not reading maps.
- fix result null check in read_one_map().
- Fix LDAP result leaks on error paths.
- code analysis fixes 1.
- fix not bind mounting local filesystem.
- update dir map-type patch for changed patch order.
- fix wait for master source mutex.
- fix submount shutdown race
- fix fix map source check in file lookup.
- add disable move mount configure option.

* Wed Jul 6 2011 Ian Kent <ikent@redhat.com> - 1:5.0.6-2
- add missing spec file entries for dir-type change (bz719208).

* Mon Jul 4 2011 Ian Kent <ikent@redhat.com> - 1:5.0.6-1
- update source to 5.0.6.
- fix ipv6 name for lookup fix.
- add dir map-type patch.

* Tue Jun 14 2011 Ian Kent <ikent@redhat.com> - 1:5.0.5-38
- fix lsb service name in init script (bz692963).

* Fri Mar 18 2011 Ian Kent <ikent@redhat.com> - 1:5.0.5-37
- replace GPLv3 code with GPLv2 equivalent.
 
* Thu Mar 03 2011 Ian Kent <ikent@redhat.com> - 1:5.0.5-36
- use weight only for server selection.
- fix isspace() wild card substition.
- auto adjust ldap page size.
- fix prune cache valid check.
- fix mountd vers retry.
- fix expire race.
- add lsb force-reload and try-restart.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.0.5-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 23 2010 Ian Kent <ikent@redhat.com> - 1:5.0.5-34.fc15
- revert wait for master map to be available at start.

* Mon Nov 22 2010 Ian Kent <ikent@redhat.com> - 1:5.0.5-33.fc15
- fix wait for master map to be available at start.

* Mon Nov 8 2010 Ian Kent <ikent@redhat.com> - 1:5.0.5-32.fc15
- always read file maps mount lookup map read fix.
- fix direct map not updating on reread.
- add external bind method.
- fix add simple bind auth.
- add option to dump configured automount maps.
- wait for master map to be available at start.

* Fri Aug 27 2010 Ian Kent <ikent@redhat.com> - 1:5.0.5-31.fc15
- fix status privilege error (bz627605).

* Wed Aug 18 2010 Ian Kent <ikent@redhat.com> - 1:5.0.5-30.fc15
- fix restart not working (bz624694).

* Wed Aug 11 2010 Ian Kent <ikent@redhat.com> - 1:5.0.5-29
- remove ERR_remove_state() openssl call.

* Tue Aug 10 2010 Ian Kent <ikent@redhat.com> - 1:5.0.5-28
- remove extra read master map call.
- remove extra cache create call in master_add_map_source().
- fix error handing in do_mount_indirect().
- expire thread use pending mutex.
- explicity link against the Kerberos library.
- remove some log message duplication for verbose logging.

* Mon May 24 2010 Ian Kent <ikent@redhat.com> - 1:5.0.5-27.fc14
- fix master map source server unavailable handling.
- add autofs_ldap_auth.conf man page.
- fix random selection for host on different network.
- make redhat init script more lsb compliant.
- don't hold lock for simple mounts.
- fix remount locking.
- fix wildcard map entry match.
- fix parse_sun() module init.
- dont check null cache on expire.
- fix null cache race.
- fix cache_init() on source re-read.
- fix mapent becomes negative during lookup.
- check each dc server individually.
- fix negative cache included map lookup.
- remove state machine timed wait.

* Fri Apr 30 2010 Ian Kent <ikent@redhat.com> - 1:5.0.5-26.fc14
- remove URL tag as there is not official autofs wiki (bz529804).

* Wed Apr 7 2010 Ian Kent <ikent@redhat.com> - 1:5.0.5-25.fc14
- make nfs4 default for replicated selection configuration (bz579949).
- add simple bind authentication option (bz579951).

* Fri Mar 26 2010 Ian Kent <ikent@redhat.com> - 1:5.0.5-24.fc14
- fix add locality as valid ldap master map attribute (bz575863).

* Wed Mar 17 2010 Ian Kent <ikent@redhat.com> - 1:5.0.5-22
- fix get query dn failure.
- fix ampersand escape in auto.smb.
- add locality as valid ldap master map attribute.

* Wed Mar 17 2010 Ian Kent <ikent@redhat.com> - 1:5.0.5-22
- add Conflicts to ensure we get fixed cyrus-sasl-lib for rev 21 change.

* Tue Feb 23 2010 Ian Kent <ikent@redhat.com> - 1:5.0.5-21
- add missing sasl mutex callbacks.

* Thu Feb 11 2010 Ian Kent <ikent@redhat.com> - 1:5.0.5-19
- fix segfault upon reconnect cannot find valid base dn.

* Mon Feb 1 2010 Ian Kent <ikent@redhat.com> - 1:5.0.5-17
- dont connect at ldap lookup module init.
- fix random selection option.
- fix disable timeout.
- fix strdup() return value check.

* Tue Dec 8 2009 Ian Kent <ikent@redhat.com> - 1:5.0.5-16
- fix memory leak on reload (bz545137).

* Fri Dec 4 2009 Ian Kent <ikent@redhat.com> - 1:5.0.5-14
- fix rpc fail on large export list (bz543023).

* Mon Nov 30 2009 Ian Kent <ikent@redhat.com> - 1:5.0.5-12
- check for path mount location in generic module.
- dont fail mount on access fail.

* Tue Nov 24 2009 Ian Kent <ikent@redhat.com> - 1:5.0.5-10
- fix pidof init script usage.

* Mon Nov 23 2009 Ian Kent <ikent@redhat.com> - 1:5.0.5-8
- fix timeout in connect_nb().

* Mon Nov 16 2009 Ian Kent <ikent@redhat.com> - 1:5.0.5-6
- don't use master_lex_destroy() to clear parse buffer.
- make documentation for set-log-priority clearer.

* Tue Nov 10 2009 Ian Kent <ikent@redhat.com> - 1:5.0.5-5
- fix ext4 "preen" fsck at mount.

* Mon Nov 9 2009 Ian Kent <ikent@redhat.com> - 1:5.0.5-4
- fix stale initialization for file map instance patch was not applied.

* Tue Nov 3 2009 Ian Kent <ikent@redhat.com> - 1:5.0.5-3
- fix stale initialization for file map instance.

* Tue Oct 6 2009 Ian Kent <kent@redhat.com> - 1:5.0.5-2
- fix included map read fail handling.
- refactor ldap sasl authentication bind to eliminate extra connect
  causing some servers to reject the request. 
- add mount wait parameter to allow timeout of mount requests to
  unresponsive servers.
- special case cifs escape handling.
- fix libxml2 workaround configure.
- more code analysis corrections (and fix a typo in an init script).
- fix backwards #ifndef INET6.

* Fri Sep 4 2009 Ian Kent <ikent@redhat.com> - 1:5.0.5-1
- update source to latest upstream version.
  - this is essentially a consolidation of the patches already in this rpm.
- add dist tag to match latest RHEL-5 package tag format.

* Thu Sep 3 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-39
- fix libxml2 non-thread-safe calls.
- fix direct map cache locking.
- fix patch "dont umount existing direct mount on reread" deadlock.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.0.4-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-34
- fix typo in patch to allow dumping core.

* Wed Jul 15 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-32
- fix an RPC fd leak.
- don't block signals we expect to dump core.
- fix pthread push order in expire_proc_direct().

* Fri Jun 12 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-30
- fix incorrect dclist free.
- srv lookup handle endianness.
- fix bug introduced by library reload changes which causes autofs to
  not release mount thread resources when using submounts.
- fix notify mount message path.
- try harder to work out if we created mount point at remount.
- fix double free in do_sasl_bind().
- manual umount recovery fixes.
- fix map type info parse error.

* Mon May 18 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-28
- use intr option as hosts mount default.
- sync kernel includes with upstream kernel.
- dont umount existing direct mount on master re-read.
- fix incorrect shutdown introduced by library relaod fixes.
- improve manual umount recovery.
- dont fail on ipv6 address when adding host.
- always read file maps multi map fix.
- always read file maps key lookup fixes.
- add support for LDAP_URI="ldap:///<domain db>" SRV RR lookup.

* Thu Apr 16 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-26
- fix lsb init script header.
- fix memory leak reading ldap master map.
- fix st_remove_tasks() locking.
- reset flex scanner when setting buffer.
- zero s_magic is valid.

* Mon Mar 30 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-24
- clear rpc client on lookup fail.

* Fri Mar 20 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-23
- fix call restorecon when misc device file doesn't exist.

* Wed Mar 18 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-22
- use misc device ioctl interface by default, if available.

* Tue Mar 17 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-21
- fix file map lookup when reading included or nsswitch sources.
  - a regression introduced by file map lookup optimisation in rev 9.

* Fri Mar 13 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-20
- add LSB init script parameter block.

* Fri Mar 13 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-19
- another easy alloca replacements fix.

* Thu Mar 12 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-18
- fix return start status on fail.
- fix double free in expire_proc().

* Wed Feb 25 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-17
- fix bad token declaration in master map parser.

* Wed Feb 25 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-16
- correct mkdir command in %%install section, bz481132.

* Tue Feb 24 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-15
- fix array out of bounds accesses and cleanup couple of other alloca() calls.
- Undo mistake in copy order for submount path introduced by rev 11 patch.
- add check for alternate libxml2 library for libxml2 tsd workaround.
- add check for alternate libtirpc library for libtirpc tsd workaround.
- cleanup configure defines for libtirpc.
- add WITH_LIBTIRPC to -V status report.
- add libtirpc-devel to BuildRequires.
- add nfs mount protocol default configuration option.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Ian Kent <ikent@redhat.com> - 5.0.4-10
- fix mntent.h not included before use of setmntent_r().

* Mon Feb 16 2009 Ian Kent <ikent@redhat.com> - 5.0.4-9
- fix hosts map use after free.
- fix uri list locking (again).
- check for stale SASL credentials upon connect fail.
- add "forcestart" and "forcerestart" init script options to allow
  use of 5.0.3 strartup behavior if required.
- always read entire file map into cache to speed lookups.
- make MAX_ERR_BUF and PARSE_MAX_BUF use easier to audit.
- make some easy alloca replacements.
- update to configure libtirpc if present.
- update to provide ipv6 name and address support.
- update to provide ipv6 address parsing.

* Thu Feb 5 2009 Ian Kent <ikent@redhat.com> - 5.0.4-8
- rename program map parsing bug fix patch.
- use CLOEXEC flag functionality for setmntent also, if present.

* Wed Jan 21 2009 Jeff Moyer <jmoyer@redhat.com> - 5.0.4-6
- fix a bug in the program map parsing routine

* Thu Jan 15 2009 Ian Kent <kent@redhat.com> - 5.0.4-5
- fix negative caching of non-existent keys.
- fix ldap library detection in configure.
- use CLOEXEC flag functionality if present.
- fix select(2) fd limit.
- make hash table scale to thousands of entries.

* Wed Dec 3 2008 Ian Kent <kent@redhat.com> - 5.0.4-4
- fix nested submount expire deadlock.

* Wed Nov 19 2008 Ian Kent <kent@redhat.com> - 5.0.4-3
- fix libxml2 version check for deciding whether to use workaround.

* Tue Nov 11 2008 Ian Kent <kent@redhat.com> - 5.0.4-2
- Fix tag confusion.

* Tue Nov 11 2008 Ian Kent <kent@redhat.com> - 5.0.4-1
- Upstream source version 5.0.4.

* Tue Nov 11 2008 Ian Kent <kent@redhat.com> - 5.0.3-32
- correct buffer length setting in autofs-5.0.3-fix-ifc-buff-size-fix.patch.

* Sun Nov 2 2008 Ian Kent <kent@redhat.com> - 5.0.3-30
- fix segv during library re-open.
- fix incorrect pthreads condition handling for expire requests.
- fix master map lexer eval order.
- fix bad alloca usage.

* Thu Oct 23 2008 Ian Kent <ikent@redhat.com> - 5.0.3-28
- don't close file handle for rootless direct mounti-mount at mount.
- wait submount expire thread completion when expire successful.
- add inadvertantly ommitted server list locking in LDAP module.

* Fri Oct 10 2008 Ian Kent <ikent@redhat.com> - 5.0.3-26
- add map-type-in-map-name fix patch to sync with upstream and RHEL.
- don't readmap on HUP for new mount.
- add NIS_PARTIAL to map entry not found check and fix use after free bug.

* Fri Sep 26 2008 Ian Kent <ikent@redhat.com> - 5.0.3-25
- fix fd leak at multi-mount non-fatal mount fail.
- fix incorrect multi-mount mountpoint calcualtion.

* Fri Sep 19 2008 Ian Kent <ikent@redhat.com> - 5.0.3-23
- add upstream bug fixes
  - bug fix for mtab check.
  - bug fix for zero length nis key.
  - update for ifc buffer handling.
  - bug fix for kernel automount handling.
- warning: I found a bunch of patches that were present but not
  being applied.
  
* Mon Aug 25 2008 Ian Kent <ikent@redhat.com> - 5.0.3-21
- add upstream bug fix patches
  - add command line option to override is running check.
  - don't use proc fs for is running check.
  - fix fail on included browse map not found.
  - fix incorrect multi source messages.
  - clear stale flag on map read.
  - fix proximity other rpc ping timeout.
  - refactor mount request vars code.
  - make handle_mounts startup condition distinct.
  - fix submount shutdown handling.
  - try not to block on expire.
  - add configuration paramter UMOUNT_WAIT.
  - fix multi mount race.
  - fix nfs4 colon escape handling.
  - check replicated list after probe.
  - add replicated server selection debug logging.
  - update replicated server selection documentation.
  - use /dev/urandom instead of /dev/random.
  - check for mtab pointing to /proc/mounts.
  - fix interface config buffer size.
  - fix percent hack heap corruption.

* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 5.0.3-19
- change conflicts to requires
- fix license tag

* Mon Jun 30 2008 Ian Kent <ikent@redhat.com> - 5.0.3-18
- don't abuse the ap->ghost field on NFS mount.
- multi-map doesn't pickup NIS updates automatically.
- eliminate redundant DNS name lookups.
- mount thread create condition handling fix.
- allow directory create on NFS root.
- check direct mount path length.
- fix incorrect in check in get user info.
- fix a couple of memory leaks.

* Wed May 14 2008 Ian Kent <ikent@redhat.com> - 5.0.3-16
- update patches, documentation and comments only change.
- rename patch and add to CVS.

* Mon May 12 2008 Ian Kent <ikent@redhat.com> - 5.0.3-14
- check for nohide mounts (bz 442618).
- ignore nsswitch sources that aren't supported (bz 445880).

* Thu Apr 17 2008 Ian Kent <ikent@redhat.com> - 5.0.3-13
- fix typo in patch for incorrect pthreads condition handling patch.

* Mon Apr 14 2008 Ian Kent <ikent@redhat.com> - 5.0.3-12
- fix incorrect pthreads condition handling for mount requests.

* Tue Apr 1 2008 Ian Kent <ikent@redhat.com> - 5.0.3-11
- and another try at fixing lexer matching map type in map name.

* Sun Mar 30 2008 Ian Kent <ikent@redhat.com> - 5.0.3-10
- another try a fixing lexer matching map type in map name.

* Wed Mar 26 2008 Ian Kent <ikent@redhat.com> - 5.0.3-9
- fix lexer ambiguity in match when map type name is included in map name.

* Mon Mar 24 2008 Ian Kent <ikent@redhat.com> - 5.0.3-8
- revert miscellaneous device node related patches.
- add missing check for zero length NIS key.
- fix incorrect match of map type name when included in map name.
- update rev 7 sasl callbacks patch.

* Thu Mar 20 2008 Ian Kent <ikent@redhat.com> - 5.0.3-7
- add patch to initialize sasl callbacks unconditionally on autofs
  LDAP lookup library load.

* Mon Feb 25 2008 Ian Kent <ikent@redhat.com> - 5.0.3-6
- fix expire calling kernel more often than needed.
- fix unlink of mount tree incorrectly causing autofs mount fail.
- add miscellaneous device node interface library.
- use miscellaneous device node, if available, for active restart.
- device node and active restart fixes.
- update is_mounted to use device node ioctl, if available.

* Fri Feb 1 2008 Ian Kent <ikent@redhat.com> - 5.0.3-5
- another fix for don't fail on empty master map.

* Fri Jan 25 2008 Ian Kent <ikent@redhat.com> - 5.0.3-4
- correction to the correction for handling of LDAP base dns with spaces.
- avoid using UDP for probing NFSv4 mount requests.
- use libldap instead of libldap_r.

* Mon Jan 21 2008 Ian Kent <ikent@redhat.com> - 5.0.3-3
- catch "-xfn" map type and issue "no supported" message.
- another correction for handling of LDAP base dns with spaces.

* Mon Jan 14 2008 Ian Kent <ikent@redhat.com> - 5.0.3-2
- correct configure test for ldap page control functions.

* Mon Jan 14 2008 Ian Kent <ikent@redhat.com> - 5.0.3-1
- update source to version 5.0.3.

* Fri Dec 21 2007 Ian Kent <ikent@redhat.com> - 5.0.2-25
- Bug 426401: CVE-2007-6285 autofs default doesn't set nodev in /net [rawhide]
  - use mount option "nodev" for "-hosts" map unless "dev" is explicily specified.

* Tue Dec 18 2007 Ian Kent <ikent@redhat.com> - 5.0.2-23
- Bug 397591 SELinux is preventing /sbin/rpc.statd (rpcd_t) "search" to <Unknown> (sysctl_fs_t).
  - prevent fork between fd open and setting of FD_CLOEXEC.

* Thu Dec 13 2007 Ian Kent <ikent@redhat.com> - 5.0.2-21
- Bug 421371: CVE-2007-5964 autofs defaults don't restrict suid in /net [rawhide]
  - use mount option "nosuid" for "-hosts" map unless "suid" is explicily specified.

* Thu Dec  6 2007 Jeremy Katz <katzj@redhat.com> - 1:5.0.2-19
- rebuild for new ldap

* Tue Nov 20 2007 Ian Kent <ikent@redhat.com> - 5.0.2-18
- fix schema selection in LDAP schema discovery.
- check for "*" when looking up wildcard in LDAP.
- fix couple of edge case parse fails of timeout option.
- add SEARCH_BASE configuration option.
- add random selection as a master map entry option.
- re-read config on HUP signal.
- add LDAP_URI, LDAP_TIMEOUT and LDAP_NETWORK_TIMEOUT configuration options.
- fix deadlock in submount mount module.
- fix lack of ferror() checking when reading files.
- fix typo in autofs(5) man page.
- fix map entry expansion when undefined macro is present.
- remove unused export validation code.
- add dynamic logging (adapted from v4 patch from Jeff Moyer).
- fix recursive loopback mounts (Matthias Koenig).
- add map re-load to verbose logging.
- fix handling of LDAP base dns with spaces.
- handle MTAB_NOTUPDATED status return from mount.
- when default master map, auto.master, is used also check for auto_master.
- update negative mount timeout handling.
- fix large group handling (Ryan Thomas).
- fix for dynamic logging breaking non-sasl build (Guillaume Rousse).
- eliminate NULL proc ping for singleton host or local mounts.

* Mon Sep 24 2007 Ian Kent <ikent@redhat.com> - 5.0.2-16
- add descriptive comments to config about LDAP schema discovery.
- work around segfault at exit caused by libxml2.
- fix foreground logging (also fixes shutdown needing extra signal bug).

* Wed Sep 5 2007 Ian Kent <ikent@redhat.com> - 5.0.2-15
- fix LDAP schema discovery.

* Tue Aug 28 2007 Ian Kent <ikent@redhat.com> - 5.0.2-14
- update patch to prevent failure on empty master map.
- if there's no "automount" entry in nsswitch.conf use "files" source.
- add LDAP schema discovery if no schema is configured.

* Wed Aug 22 2007 Ian Kent <ikent@redhat.com> - 5.0.2-13
- fix "nosymlink" option handling and add desription to man page.

* Tue Aug 21 2007 Ian Kent <ikent@redhat.com> - 5.0.2-12
- change random multiple server selection option name to be consistent
  with upstream naming.

* Tue Aug 21 2007 Ian Kent <ikent@redhat.com> - 5.0.2-11
- don't fail on empty master map.
- add support for the "%" hack for case insensitive attribute schemas.

* Mon Jul 30 2007 Ian Kent <ikent@redhat.com> - 5.0.2-10
- mark map instances stale so they aren't "cleaned" during updates.
- fix large file compile time option.

* Fri Jul 27 2007 Ian Kent <ikent@redhat.com> - 5.0.2-9
- fix version passed to get_supported_ver_and_cost (bz 249574).

* Tue Jul 24 2007 Ian Kent <ikent@redhat.com> - 5.0.2-8
- fix parse confusion between attribute and attribute value.

* Fri Jul 20 2007 Ian Kent <ikent@redhat.com> - 5.0.2-7
- fix handling of quoted slash alone (bz 248943).

* Wed Jul 18 2007 Ian Kent <ikent@redhat.com> - 5.0.2-6
- fix wait time resolution in alarm and state queue handlers (bz 247711).

* Mon Jul 16 2007 Ian Kent <ikent@redhat.com> - 5.0.2-5
- fix mount point directory creation for bind mounts.
- add quoting for exports gathered by hosts map.

* Mon Jun 25 2007 Ian Kent <ikent@redhat.com> - 5.0.2-4
- update multi map nsswitch patch.

* Mon Jun 25 2007 Ian Kent <ikent@redhat.com> - 5.0.2-3
- add missing "multi" map support.
- add multi map nsswitch lookup.

* Wed Jun 20 2007 Ian Kent <ikent@redhat.com> - 5.0.2-2
- include krb5.h in lookup_ldap.h (some openssl doesn't implicitly include it).
- correct initialization of local var in parse_server_string.

* Mon Jun 18 2007 Ian Kent <ikent@redhat.com> - 5.0.2-1
- Update to upstream release 5.0.2.

* Tue Jun 12 2007 Ian Kent <ikent@redhat.com> - 5.0.1-16
- add ldaps support.
  - note: it's no longer possible to have multiple hosts in an ldap map spec.
  - note: to do this you need to rely on the ldap client config.

* Thu Jun 7 2007 Ian Kent <ikent@redhat.com> - 5.0.1-14
- fix deadlock in alarm manager module.

* Sun Jun 3 2007 Ian Kent <ikent@redhat.com> - 5.0.1-12
- correct mistake in logic test in wildcard lookup.

* Mon May 7 2007 Ian Kent <ikent@redhat.com> - 5.0.1-10
- fix master map lexer to admit "." in macro values.

* Tue Apr 17 2007 Ian Kent <ikent@redhat.com> - 5.0.1-9
- upstream fix for filesystem is local check.
- disable exports access control check (bz 203277).
- fix patch to add command option for set a global mount options (bz 214684).

* Mon Apr 16 2007 Ian Kent <ikent@redhat.com> - 5.0.1-8
- add configuration variable to control appending of global options (bz 214684).
- add command option to set a global mount options string (bz 214684).

* Tue Apr 3 2007 Ian Kent <ikent@redhat.com> - 5.0.1-7
- fix "null" domain netgroup match for "-hosts" map.

* Thu Mar 29 2007 Ian Kent <ikent@redhat.com> - 5.0.1-6
- fix directory creation for browse mounts.
- fix wildcard map handling and improve nsswitch source map update.

* Fri Mar 16 2007 Ian Kent <ikent@redhat.com> - 5.0.1-5
- drop "DEFAULT_" prefix from configuration names.
- add option to select replicated server at random (instead of
  ping response time) (bz 227604).
- fix incorrect cast in directory cleanup routines (bz 231864).

* Thu Mar 8 2007 Ian Kent <ikent@redhat.com> - 5.0.1-4
- fixed numeric export match (bz 231188).

* Thu Mar 1 2007 Ian Kent <ikent@redhat.com> - 5.0.1-3
- change file map lexer to allow white-space only blank lines (bz 229434).

* Fri Feb 23 2007 Ian Kent <ikent@redhat.com> - 5.0.1-2
- update "@network" matching patch.

* Thu Feb 22 2007 Ian Kent <ikent@redhat.com> - 5.0.1-1
- update to release tar.
- fix return check for getpwuid_r and getgrgid_r.
- patch to give up trying to update exports list while host is mounted.
- fix to "@network" matching. 
- patch to check for fstab update and retry if not updated.

* Tue Feb 20 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.24
- add "condrestart" to init script (bz 228860).
- add "@network" and .domain.name export check.
- fix display map name in mount entry for "-hosts" map.

* Fri Feb 16 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.22
- fix localhost replicated mounts not working (bz 208757).

* Wed Feb 14 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.20
- correct return status from do_mkdir (bz 223480).

* Sat Feb 10 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.18
- update the "task done race" patch to fix a deadlock.
- added URL tag.
- removed obsoletes autofs-ldap.
- replaced init directory paths with %%{_initrddir} macro.

* Fri Feb 9 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.17
- make use of spaces and tabs in spec file consistent.
- escape embedded macro text in %%changelog.
- eliminate redundant %%version and %%release.
- remove redundant conditional check from %%clean.
- remove redundant exit from %%preun.
- correct %%defattr spec.
- remove empty %%doc and redundant %%dir misc lines.
- combine program module spec lines into simpler one line form.

* Tue Feb 6 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.15
- fix race when setting task done (bz 227268).

* Mon Jan 29 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.13
- make double quote handing consistent (at least as much as we can).
- fix handling of trailing white space in wildcard lookup (forward port bz 199720).
- check fqdn of each interface when matching export access list (bz 213700).

* Thu Jan 18 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.11
- correct check for busy offset mounts before offset umount (bz 222872).

* Wed Jan 17 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.9
- fix another expire regression introduced in the "mitigate manual umount"
  patch (bz 222872).

* Mon Jan 15 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.7
- ignore "winbind" if it appears in "automount" nsswitch.conf (bz 214632).

* Wed Jan 10 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.5
- remove fullstop from Summary tag.
- change Buildroot to recommended form.
- replace Prereq with Requires.

* Tue Jan 9 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.3
- remove redundant rpath link option (prep for move to Extras).

* Tue Jan 9 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.1
- consolidate to rc3.
- fix typo in Fix typo in var when removing temp directory (bz 221847).

* Wed Dec 27 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.41
- fix nonstrict multi-mount handling (bz 219383).
- correct detection of duplicate indirect mount entries (bz 220799).

* Thu Dec 14 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.38
- update master map tokenizer to admit "slasify-colons" option.
- update location validation to accept "_" (bz 219445).
- set close-on-exec flag on open sockets (bz 215757).

* Mon Dec 11 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.35
- update "replace-tempnam" patch to create temp files in sane location.

* Mon Dec 11 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.34
- change mount "device" from "automount" to the map name.
- check for buffer overflow in mount_afs.c.
- replace tempnam with mkdtemp.

* Sun Dec 10 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.33
- expand export access checks to include missing syntax options.
- make "-hosts" module try to be sensitive to exports list changes.

* Thu Dec 7 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.32
- remove ability to use multiple indirect mount entries in master
  map (bz 218616).

* Wed Dec 6 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.29
- alter nfs4 host probing to not use portmap lookup and add options
  check for "port=" parameter (bz 208757).
- correct semantics of "-null" map handling (bzs 214800, 208091).

* Sat Nov 25 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.26
- fix parsing of bad mount mount point in master map (bz 215620).
- fix use after free memory access in cache.c and lookup_yp.c (bz 208091).
- eliminate use of pthread_kill to detect task completion (bz 208091).

* Sun Nov 12 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.23
- fix tokenizer to distinguish between global option and dn string (bz 214684).
- fix incorrect return from spawn.

* Wed Nov 8 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.21
- mitigate manual umount of automounts where possible.
- fix multiply recursive bind mounts.
- check kernel module version and require 5.00 or above.
- fix expire regression introduced in the "mitigate manual umount" patch.
- still more on multiply recursive bind mounts.

* Mon Oct 30 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.20
- Update patch for changed semantics of mkdir in recent kernels.
- fix macro table locking (bz 208091).
- fix nsswitch parser locking (bz 208091).
- allow only one master map read task at a time.
- fix misc memory leaks.

* Wed Oct 25 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.19
- deal with changed semantics of mkdir in recent kernels.

* Fri Oct 20 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.16
- fix get_query_dn not looking in subtree for LDAP search (missed
  econd occurance).
- allow additional common LDAP attributes in map dn.
- Resolves: rhbz#205997

* Mon Oct 16 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.13
- fix parsing of numeric host names in LDAP map specs (bz 205997).

* Mon Oct 16 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.12
- fix "-fstype=nfs4" server probing (part 2 of bz 208757).
- set close-on-exec flag on open files where possible (bz 207678).

* Fri Oct 13 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.11
- fix file handle leak in nsswitch parser (bz 207678).
- fix memory leak in mount and expire request processing (bz 207678).
- add additional check to prevent running of cancelled tasks.
- fix potential file handle leakage in rpc_subs.c for some failure
  cases (bz 207678).
- fix file handle leak in included map lookup (bz 207678).

* Sat Oct 7 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.10
- fix get_query_dn not looking in subtree for LDAP search.
- allow syntax "--timeout <secs>" for backward compatibility
  (bz 193948).
- make masked_match independent of hostname for exports comparison
  (bz 209638).

* Thu Oct 5 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.9
- fix "-fstype=nfs4" handling (bz 208757).

* Wed Sep 27 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.8
- review and fix master map options update for map reload.

* Wed Sep 27 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.7
- make default installed master map for /net use "-hosts" instead
  of auto.net.
- fix included map recursive map key lookup.

* Mon Sep 25 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.6
- remove unused option UNDERSCORETODOT from default config files.

* Mon Sep 25 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.5
- fix LDAP lookup delete cache entry only if entry doesn't exist.
- add missing socket close in replicated host check (Jeff Moyer).

* Wed Sep 20 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.4
- fix cache entrys not being cleaned up on submount expire.

* Sun Sep 17 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.3
- fix include check full patch for file map of same name.

* Wed Sep 13 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.2
- fix handling of autofs specific mount options (bz 199777).

* Fri Sep 1 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.1
- consolidate to rc2.
- fix colon escape handling.
- fix recusively referenced bind automounts.
- update kernel patches.

* Fri Aug 25 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.17
- fix task cancelation at shutdown (more)
- fix concurrent mount and expire race with nested submounts.

* Sun Aug 20 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.16
- fix included map lookup.
- fix directory cleanup on expire.
- fix task cancelation at shutdown.
- fix included map wild card key lookup.

* Wed Aug 16 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.15
- expire individual submounts.
- add ino_index locking.
- fix nested submount expiring away when pwd is base of submount.
- more expire re-work to cope better with shutdown following cthon tests.
- allow hostname to start with numeric when validating.

* Mon Aug 7 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.14
- remove SIGCHLD handler because it is no longer needed and was
  causing expire problems.
- alter expire locking of multi-mounts to lock sub-tree instead of
  entire tree.
- review verbose message feedback and update.
- correction for expire of multi-mounts.
- spelling corrections to release notes (Jeff Moyer).
- add back sloppy mount option, removed for Connectathon testing.
- disable mtab locking again.

* Fri Aug 4 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.13
- tidy up directory cleanup and add validation check to rmdir_path.

* Fri Aug 4 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.12
- enable mtab locking until I can resolve the race with it.

* Fri Aug 4 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.11
- cthon fix expire of wildcard and program mounts broken by recent
  patches.

* Thu Aug 3 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.10
- cthon corrections for shutdown patch below and fix shutdown expire.

* Wed Aug 2 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.9
- cthon fix some shutdown races.

* Thu Jul 27 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.8
- Fix compile error.

* Thu Jul 27 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.7
- cthon fix expire of various forms of nested mounts.

* Mon Jul 24 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.6
- cthon more parser corrections and attempt to fix multi-mounts
  with various combinations of submounts (still not right).

* Wed Jul 19 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.5
- Add conflicts kernel < 2.6.17.
- Fix submount operation broken by connectathon updates.

* Wed Jul 19 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.4
- Correction to host name validation test for connectathon tests.

* Wed Jul 19 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.3
- More code cleanup and corrections for connectathon tests.

* Wed Jul 19 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.2
- Code cleanup and fixes for connectathon tests.

* Thu Jul 13 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.1
- Update version label to avoid package update problems.

* Thu Jul 13 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta6-8
- add cacheing of negative lookups to reduce unneeded map
  lookups (bz 197746 part 2).

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:5.0.0_beta6-7.1
- rebuild

* Tue Jul 11 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta6-7
- correct directory cleanup in mount modules.
- merge key and wildcard LDAP query for lookups (bz 197746).

* Sat Jul 8 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta6-6
- correct test for libhesiod.

* Fri Jul 7 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta6-5
- correct auto.net installed as auto.smb.
- update LDAP auth - add autodectect option.

* Wed Jul 5 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta6-4
- correct shutdown log message print.
- correct auth init test when no credentials required.

* Tue Jul 4 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta6-3
- correct test for existence of auth config file.

* Mon Jul 3 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta6-2
- merge LDAP authentication update for GSSAPI (Jeff Moyer).
- update default auth config to add options documenetation (Jeff Moyer).
- workaround segfaults at exit after using GSSAPI library.
- fix not checking return in init_ldap_connection (jeff Moyer).

* Thu Jun 29 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta6-1
- consolidate to beta6, including:
  - mode change update for config file.
  - correction to get_query_dn fix from beta5-4.

* Wed Jun 28 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta5-6
- cleanup defaults_read_config (Jeff Moyer).

* Tue Jun 27 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta5-5
- allow global macro defines to override system macros.
- correct spelling error in default config files missed by
  previous update.
- misc correctness and a memory leak fix.

* Mon Jun 26 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta5-4
- correct spelling error in default config.
- fix default auth config not being installed.
- change LDAP query method as my test db was incorrect.
- change ldap defaults code to handle missing auth config.
- fix mistake in parsing old style LDAP specs.
- update LDAP so that new query method also works for old syntax.

* Fri Jun 23 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta5-3
- lookup_init cleanup and fix missed memory leak.
- use nis map order to check if update is needed.
- fix couple of memory leaks in lookup_yp.c.
- fix pasre error in replicated server module.

* Wed Jun 21 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta5-2
- Add openssl-devel to the BuildRequires, as it is needed for the LDAP
  authentication bitsi also.

* Tue Jun 20 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta5-1
- promote to beta5.

* Tue Jun 20 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-14
- fix directory cleanup at exit.

* Mon Jun 19 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-13
- Change LDAP message severity from crit to degug (bz# 183893).
- Corrections to INSTALL and README.v5.release.
- Add patch to fix segv on overlength map keys in file maps (Jeff Moter).
- Add patch to restrict scanning of /proc to pid directories only (Jeff Moyer).

* Thu Jun 15 2006 Jeff Moyer <jmoyer@redhat.com> - 5.0.0_beta4-12
- Change BuildPrereq to BuildRequires as per the package guidelines.
- Add libxml2-devel to the BuildRequires, as it is needed for the LDAP
  authentication bits.

* Wed Jun 14 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-11
- add export access list matching to "hosts" lookup module (bz # 193585).

* Tue Jun 13 2006 Jeff Moyer <jmoyer@redhat.com> - 5.0.0_beta4-10
- Add a BuildPrereq for cyrus-sasl-devel

* Tue Jun 13 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-9
- move autofs4 module loading back to init script (part bz # 194061).

* Mon Jun 12 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-8
- fix handling of master map entry update (bz # 193718).
- fix program map handling of invalid multi-mount offsets.

* Sat Jun 10 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-7
- fix context init error (introduced by memory leak patch).

* Fri Jun 9 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-6
- add free for working var in get_default_logging.
- add inialisation for kver in autofs_point struct.
- fix sources list corruption in check_update_map_sources.
- fix memory leak in walk_tree.
- fix memory leak in rpc_portmap_getport and rpc_ping_proto.
- fix memory leak in initialisation of lookup modules.

* Thu Jun 8 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-5
- misc fixes for things found while investigating map re-read problem.

* Wed Jun 7 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-4
- check base of offset mount tree is not a mount before umounting
  its offsets.
- fix replicated mount parse for case where last name in list
  fails lookup.
- correct indirect mount expire broken by the wildcard lookup fix.
- fix up multi-mount handling when wildcard map entry present.

* Mon Jun 5 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-3
- correct config names in default.c (jpro@bas.ac.uk).

* Mon Jun 5 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-2
- re-instate v4 directory cleanup (bz# 193832 again).
- backout master map lookup changes made to beta3.
- change default master map from /etc/auto.master to auto.master
  so that we always use nsswitch to locate master map.
- change default installed master map to include "+auto.master"
  to pickup NIS master map (all bz# 193831 again).

* Fri Jun 2 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-1
- update to beta4.
- should address at least bzs 193798, 193770, 193831 and
  possibly 193832.

* Mon May 29 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta3-6
- add back test for nested mount in program map lookup.
  - I must have commented this out for a reason. I guess we'll
    find out soon enough.

* Mon May 29 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta3-5
- fix handling of autofs filesystem mount fail on init.

* Sat May 27 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta3-4
- updated hesiod patch.

* Sat May 27 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta3-3
- update hesiod module (Jeff Moyer).
  - add mutex to protect against overlapping mount requests.
  - update return from mount request to give more sensible NSS_*
    values.

* Fri May 26 2006 Jeff Moyer <jmoyer@redhat.com> - 1:5.0.0_beta3-2
- Fix the install permissions for auto.master and auto.misc.

* Thu May 25 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta3-1
- update source to version 5.0.0_beta3.
- add patch to remove extra debug print.
- add patch to
  - fix memory alloc error in nis lookup module.
  - add "_" to "." mapname translation to nis lookup module.
- add patch to add owner pid to mount list struct.
- add patch to disable NFSv4 when probing hosts (at least foe now).
- add patch to fix white space handling in replicated server selection code.
- add patch to prevent striping of debug info macro patch (Jeff Moyer).
- add patch to add sanity checks on rmdir_path and unlink (Jeff Moyer).
- add patch to fix e2fsck error code check (Jeff Moyer).

* Tue May 16 2006 Ian Kent <ikent@redhat.com> - 1:4.1.4-23
- add patch to ignore the "bg" and "fg" mount options as they
  aren't relevant for autofs mounts (bz #184386).

* Tue May 2 2006 Ian Kent <ikent@redhat.com> - 1:4.1.4-20
- add patch to use "cifs" instead of smbfs and escape speces
  in share names (bz #163999, #187732).

* Tue Apr 11 2006 Ian Kent <ikent@redhat.com> - 1:4.1.4-18
- Add patch to allow customization of arguments to the
  autofs-ldap-auto-master program (bz #187525).
- Add patch to escap "#" characters in exports from auto.net
  program mount (bz#178304).

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1:4.1.4-16.2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1:4.1.4-16.2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Feb 1 2006 Ian Kent <ikent@redhat.com> - 1:4.1.4-16.2
- Add more general patch to translate "_" to "." in map names. (bz #147765)

* Wed Jan 25 2006 Ian Kent <ikent@redhat.com> - 1:4.1.4-16.1
- Add patch to use LDAP_DEPRICATED compile option. (bz #173833)

* Tue Jan 17 2006 Ian Kent <ikent@redhat.com> - 1:4.1.4-16
- Replace check-is-multi with more general multi-parse-fix.
- Add fix for premature return when waiting for lock file.
- Update copyright declaration for reentrant-syslog source.
- Add patch for configure option to disable locking during mount.
  But don't disable locking by default.
- Add ability to handle automount schema used in Sun directory server.
- Quell compiler warning about getsockopt parameter.
- Quell compiler warning about yp_order parameter.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Nov 17 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-14
- Removed the /misc entry from the default auto.master.  auto.misc has
  an entry for the cdrom device, and the preferred method of mounting the
  cd is via udev/hal.

* Mon Nov  7 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-13
- Changed to sort -k 1, since that should be the same as +0.

* Thu Nov  3 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-12
- The sort command no longer accepts options of the form "+0".  This broke
  auto.net, so the option was removed.  Fixes bz #172111.

* Wed Oct 26 2005  <jmoyer@redhat.com> - 1:4.1.4-11
- Check the return code of is_local_addr in get_best_mount. (bz #169523)

* Wed Oct 26 2005  <jmoyer@redhat.com> - 1:4.1.4-10
- Fix some bugs in the parser
- allow -net instead of /etc/auto.net
- Fix a buffer overflow with large key lengths
- Don't allow autofs to unlink files, only to remove directories
- change to the upstream reentrant syslog patch from the band-aid deferred
  syslog patch.
- Get rid of the init script patch that hard-coded the release to redhat.
  This should be handled properly by all red hat distros.

* Wed May  4 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-8
- Add in the deferred syslog patch.  This fixes a hung automounter issue
  related to unsafe calls to syslog in signal handler context.

* Tue May  3 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-7
- I reversed the checking for multimount entries, breaking those configs!
  This update puts the code back the way it was before I broke it.

* Tue Apr 26 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-6
- Fix a race between mounting a share and updating the cache in the parent
  process.  If the mount completed first, the parent would not expire the
  stale entry, leaving it first on the list.  This causes map updates to not
  be recognized (well, worse, they are recognized after the first expire, but
  not subsequent ones).  Fixes a regression, bug #137026 (rhel3 bug).

* Fri Apr 15 2005 Chris Feist <cfeist@redhat.com> - 1:4.1.4-5
- Fixed regression with -browse not taking effect.

* Wed Apr 13 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-4
- Finish up with the merge breakage.
- Temporary fix for the multimount detection code.  It seems half-baked.

* Wed Apr 13 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-3
- Fix up the one-auto-master patch.  My "improvements" had side-effects.

* Wed Apr 13 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-2
- Import 4.1.4 and merge.

* Mon Apr  4 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-123
- Add in an error case that was omitted in the multi-over patch.
- Update our auto.net to reflect the changes that went into 4.1.4_beta2.
  This fixes a problem seen by at least one customer where a malformed entry
  appeared first in the multimount list, thus causing the entire multimount
  to be ignored.  This new auto.net places that entry at the end, purely by
  luck, but it fixes the problem in this one case.

* Thu Mar 31 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-119
- Merge in the multi-over patch.  This resolves an issue whereby multimounts
  (such as those used for /net) could be processed in the wrong order,
  resulting in directories not showing up in a multimount tree.  The fix
  is to process these directories in order, shortest to longer path.

* Wed Mar 23 2005 Chris Feist <cfeist@redhat.com> - 1:4.1.3-115
- Fixed regression causing any entries after a wildcard in an
  indirect map to be ignored. (bz #151668).
- Fixed regression which caused local hosts to be mount instead
  of --bind local directories. (bz #146887)

* Thu Mar 17 2005 Chris Feist <cfeist@redhat.com> - 1:4.1.3-111
- Fixed one off bug in the submount-variable-propagation patch.
  (bz #143074)
- Fixed a bug in the init script which wouldn't find the -browse
  option if it was preceded by another option. (fz #113494)

* Mon Feb 28 2005 Chris Feist <cfeist@redhat.com> - 1:4.1.3-100
- When using ldap if auto.master doesn't exist we now check for auto_master.
  Addresses bz #130079
- When using an auto.smb map we now remove the leading ':' from the path which
  caused mount to fail in the past.  Addresses bz #147492
- Autofs now checks /etc/nsswitch.conf to determine in what order files & nis
  are checked when looking up autofs submount maps which don't specify a
  maptype.  Addresses IT #57612.

* Mon Feb 14 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-99
- Change Copyright to License in the spec file so it will build.

* Fri Feb 11 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-98
- Program maps can repeat the last character of output.  Fix this.  
  Addresses bz #138606
- Return first entry when there are duplicate keys in a map.  Addresses
  bz #140108.
- Propagate custom map variables to submounts.  Fixes bz #143074.
- Create a sysconfig variable to control whether we source only one master
  map (the way sun does), or source all maps found (which is the default for
  backwards compatibility).  Addresses bz #143126.
- Revised version of the get_best_mount patch. (#146887) cfeist@redhat.com
  The previous patch introduced a regression.  Non-replicated mounts would
  not have the white space stripped from the entry and the mount would fail.
- Handle comment characters in the middle of the automount line in
  /etc/nsswitch.conf.  Addresses bz #127457.

* Wed Feb  2 2005 Chris Feist <cfeist@redhat.com> - 1:4.1.3-94
- Stop automount from pinging hosts if there is only one host (#146887)

* Wed Feb  2 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-90
- Fix potential double free in cache_release.  This bug showed up in a
  multi-map setup.  Two calls to cache_release would result in a SIGSEGV,
  and the automount process would never exit.

* Mon Jan 24 2005 Chris Feist <cfeist@redhat.com> - 1:4.3-82
- Fixed documentation so users know that any local mounts override
  any other weighted mount.

* Mon Jan 24 2005 Chris Feist <cfeist@redhat.com> - 1:4.3-80
- Added a variable to determine if we created the directory or not
  so we don't accidently remove a directory that we didn't create when
  we stop autofs.  (bz #134399)

* Tue Jan 11 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-76
- Fix the large program map patch.

* Tue Jan 11 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-75
- Fix some merging breakages that caused the package not to build.

* Thu Jan  6 2005  <jmoyer@redhat.com> - 1:4.1.3-74
- Add in the map expiry patch
- Bring in other patches that have been committed to other branches. This 
  version should now contain all fixes we have to date
- Merge conflicts due to map expiry changes

* Fri Nov 19 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-57
- Pass a socket into clntudp_bufcreate so that we don't use up additional 
  reserved ports.  This patch, along with the socket leak fix, addresses
  bz #128966.

* Wed Nov 17 2004  <jmoyer@redhat.com> - 1:4.1.3-56
- Somehow the -browse patch either didn't get committed or got reverted.
  Fixed.

* Tue Nov 16 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-55
- Fix program maps so that they can have gt 4k characters. (Neil Horman)
  Addresses bz #138994.
- Add a space after the colon here "Starting automounter:" in init script.
  Fixes bz #138513.

* Mon Nov 15 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-53
- Make autofs understand -[no]browse.  Addresses fz #113494.

* Thu Nov 11 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-48
- Fix the umount loop device function in the init script.

* Wed Oct 27 2004 Chris Feist <cfeist@redhat.com> - 1:4.1.3-34
- Added a patch to fix the automounter failing on ldap maps
  when it couldn't get the whole map.  (ie. when the search
  limit was lower than the number of results)

* Thu Oct 21 2004 Chris Feist <cfeist@redhat.com> - 1:4.1.3-32
- Fixed the use of +ypmapname so the maps included with +ypmapname
  are used in the correct order.  (In the past the '+' entries
  were always processed after local entries.)

* Thu Oct 21 2004 Chris Feist <cfeist@redhat.com> - 1:4.1.3-31
- Fixed the duplicate map detection code to detect if maps try
  to mount on top of existing maps. 

* Wed Oct 20 2004 Chris Feist <cfeist@redhat.com> - 1:4.1.3-29
- Fixed a problem with backwards compatability. Specifying local
  maps without '/etc/' prepended to them now works. (bz #136038)

* Fri Oct 15 2004 Chris Feist <cfeist@redhat.com> - 1:4.1.3-28
- Fixed a bug which caused directories to never be unmounted. (bz #134403)

* Thu Oct 14 2004 Chris Feist <cfeist@redhat.com> - 1:4.1.3-27
- Fixed an error in the init script which caused duplicate entries to be
  displayed when asking for autofs status.

* Fri Oct  1 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-22
- Comment out map expiry (and related) patch for an FC3 build.

* Thu Sep 23 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-21
- Make local options apply to all maps in a multi-map entry.

* Tue Sep 21 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-20
- Merged my and Ian's socket leak fixes into one, smaller patch. Only
  partially addresses bz #128966.
- Fix some more echo lines for internationalization. bz #77820
- Revert the only one auto.master patch until we implement the +auto_master
  syntax.  Temporarily addresses bz #133055.

* Thu Sep  2 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-18
- Umount loopback filesystems under automount points when stopping the 
  automounter.
- Uncomment the map expiry patch.
- change a close to an fclose in lookup_file.c

* Tue Aug 31 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-17
- Add patch to support parsing nsswitch.conf to determine map sources.
- Disable this patch, and Ian's map expiry patch for a FC build.

* Tue Aug 24 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-16
- Version 3 of Ian's map expiry changes.

* Wed Aug 18 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-15
- Fix a socket leak in the rpc_subs, causing mounts to fail since we are 
  running out of port space fairly quickly.

* Wed Aug 18 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-14
- New map expiry patch from Ian.
- Fix a couple signal races.  No known problem reports of these, but they
  are holes, none-the-less.

* Tue Aug 10 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-13
- Only read one auto.master map (instead of concatenating all found sources).
- Uncomment Ian's experimental mount expiry patch.

* Fri Aug  6 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-12
- Add a sysconfig entry to disable direct map support, and set this to 
  1 by default.
- Disable the beta map expiry logic so I can build into a stable distro.
- Add defaults for all of the sysconfig variables to the init script so 
  we don't trip over user errors (i.e. deleting /etc/sysconfig/autofs).

* Wed Aug  4 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-11
- Add beta map expiry code for wider testing. (Ian Kent)
- Fix check for ghosting option.  I forgot to check for it in DAEMONOPTIONS.
- Remove STRIPDASH from /etc/sysconfig/autofs

* Mon Jul 12 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-10
- Add bad chdir patch from Ian Kent.
- Add a typo fix for the mtab lock file.
- Nuke the stripdash patch.  It didn't solve a problem.

* Tue Jun 22 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-9
- Bump revison for inclusion in RHEL 3.

* Mon Jun 21 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-8
- Change icmp ping to an rpc ping.  (Ian Kent)
- Fix i18n patch
  o Remove the extra \" from one echo line.
  o Use echo -e if we are going to do a \n in the echo string.

* Mon Jun 21 2004 Alan Cox <alan@redhat.com>
- Fixed i18n bug #107463

* Mon Jun 21 2004 Alan Cox <alan@redhat.com>
- Fixed i18n bug #107461

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Jun  5 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-4
- Perform an icmp ping request before rpc_pings, since the rpc clnt_create
  function has a builtin default timeout of 60 seconds.  This could result
  in a long delay when a server in a replicated mount setup is down.
- For non-replicated server entries, ping a host before attempting to mount.
  (Ian Kent)
- Change to %%configure.
- Put version-release into .version to allow for automount --version to
  print exact info.
- Nuke my get-best-mount patch which always uses the long timeout.  This
  should no longer be needed.
- Put name into changelog entries to make them consistent.  Add e:n-v-r
  into Florian's entry.
- Stop autofs before uninstalling

* Sat Jun 05 2004 Florian La Roche <Florian.LaRoche@redhat.de> - 1:4.1.3-3
- add a preun script to remove autofs

* Tue Jun  1 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-2
- Incorporate patch from Ian which fixes an infinite loop seen by those
  running older versions of the kernel patches (triggered by non-strict mounts
  being the default).

* Tue Jun  1 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-1
- Update to upstream 4.1.3.

* Thu May  6 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.2-6
- The lookup_yp module only dealt with YPERR_KEY, all other errors were 
  treated as success.  As a result, if the ypdomain was not bound, the 
  subprocess that starts mounts would SIGSEGV.  This is now fixed.
- Option parsing in the init script was not precise enough, sometimes matching
  filesystem options to one of --ghost, --timeout, --verbose, or --debug.  
  The option-parsing patch addresses this issue by making the regexp's much
  more precise.
- Ian has rolled a third version of the replicated mount fixes.

* Tue May  4 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.2-5
- Ian has a new fix for replicated server and multi-mounts.  Updated the 
  patch for testing.  Still beta.  (Ian Kent)

* Mon May  3 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.2-4
- Fix broken multi-mounts.  test patch.  (Ian Kent)

* Tue Apr 20 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.2-3
- Fix a call to spawnl which forgot to specify a lock file. (nphilipp)

* Wed Apr 14 2004  <jmoyer@redhat.com> - 1:4.1.2-2
- Pass --libdir= to ./configure so we get this right on 64 bit platforms that 
  support backwards compat.

* Wed Apr 14 2004  Jeff Moyer <jmoyer@redhat.com> - 1:4.1.2-1
- Change hard-coded paths in the spec file to the %%{_xxx} variety.
- Update to upstream 4.1.2.
- Add a STRIPDASH option to /etc/sysconfig/autofs which allows for
  compatibility with the Sun automounter options specification syntax in
  auto.master.  See /etc/sysconfig/autofs for more information.  Addresses
  bug 113950.

* Tue Apr  6 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.1-6
- Add the /etc/sysconfig/autofs file, and supporting infrastructure in 
  the init script.
- Add support for UNDERSCORE_TO_DOT for those who want it.
- We no longer own /net.  Move it to the filesystem package.

* Tue Mar 30 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.1-5
- Clarify documentation on direct maps.
- Send automount daemons a HUP signal during reload.  This tells them to 
  re-read maps (otherwise they use a cached version.  Patch from the autofs
  maintainer.

* Mon Mar 22 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.1-4
- Fix init script to print out failures where appropriate.
- Build the automount daemon as a PIE.

* Thu Mar 18 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.1-3
- Fix bug in get_best_mount, whereby if there is only one option, we 
  choose nothing.  This is primarily due to the fact that we pass 0 in to
  the get_best_mount function for the long timeout parameter.  So, we
  timeout trying to contact our first and only server, and never retry.

* Thu Mar 18 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.1-2
- Prevent startup if a mountpoint is already mounted.

* Thu Mar 18 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.1-1
- Update to 4.1.1, as it fixes problems with wildcards that people are 
  seeing quite a bit.

* Wed Mar 17 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.0-8
- Fix ldap init code to parse server name and options correctly.

* Tue Mar 16 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.0-7
- Moved the freeing of ap.path to cleanup_exit, as we would otherwise 
  reference an already-freed variable.

* Mon Mar 15 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.0-6
- add %%config(noreplace) for auto.* config files.

* Wed Mar 10 2004 Jeff Moyer <jmoyer@redhat.com> 1:4.1.0-5
- make the init script only recognize redhat systems.  Nalin seems to remember
  some arcane build system error that can be caused if we don't do this.

* Wed Mar 10 2004 Jeff Moyer <jmoyer@redhat.com> 1:4.1.0-4
- comment out /net and /misc from the default auto.master.  /net is important
  since in a default shipping install, we can neatly co-exist with amd.

* Wed Mar 10 2004 Jeff Moyer <jmoyer@redhat.com> 1:4.1.0-3
- Ported forward Red Hat's patches from 3.1.7 that were not already present
  in 4.1.0.
- Moving autofs from version 3.1.7 to 4.1.0

* Mon Sep 29 2003 Ian Kent <raven@themaw.net>
- Added work around for O(1) patch oddity.

* Sat Aug 16 2003 Ian Kent <raven@themaw.net>
- Fixed tree mounts.
- Corrected transciption error in autofs4-2.4.18 kernel module

* Sun Aug 10 2003 Ian Kent <raven@themaw.net>
- Checked and merged most of the RedHat v3 patches
- Fixed kernel module handling wu-ftpd login problem (again)

* Thu Aug 7 2003 Ian Kent <raven@themaw.net>
- Removed ineffective lock stuff
- Added -n to bind mount to prevent mtab update error
- Added retry to autofs umount to clean matb after fail
- Redirected messages from above to debug log and added info message
- Fixed autofs4 module reentrancy, pwd and chroot handling

* Wed Jul 30 2003 Ian Kent <raven@themaw.net>
- Fixed autofs4 ghosting patch for 2.4.19 and above (again)
- Fixed autofs directory removal on failure of autofs mount
- Fixed lock file wait function overlapping calls to (u)mount

* Sun Jul 27 2003 Ian Kent <raven@themaw.net>
- Implemented LDAP direct map handling for nisMap and automountMap schema
- Fixed autofs4 ghosting patch for 2.4.19 and above (again)
- Added locking to fix overlapping internal calls to (u)mount 
- Added wait for mtab~ to improve tolerance of overlapping external calls to (u)mount
- Fixed ghosted directory removal after failed mount attempt

* Wed May 28 2003 Ian Kent <raven@themaw.net>
- Cleaned up an restructured my added code
- Corrected ghosting problem with 2.4.19 and above
- Added autofs4 ghosting patch for 2.4.19 and above
- Implemented HUP signal to force update of ghosted maps

* Sat Mar 23 2002 Ian Kent <ian.kent@pobox.com>
- Add patch to implement directory ghosting and direct mounts
- Add patch to for autofs4 module to support ghosting

* Wed Jan 17 2001 Nalin Dahyabhai <nalin@redhat.com>
- use -fPIC instead of -fpic for modules and honor other RPM_OPT_FLAGS

* Tue Feb 29 2000 Nalin Dahyabhai <nalin@redhat.com>
- enable hesiod support over libbind

* Fri Aug 13 1999 Cristian Gafton <gafton@redhat.com>
- add patch from rth to avoid an infinite loop
