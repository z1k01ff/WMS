SELECT T.WH_TRANS_ID
      ,TO_CHAR(T.WH_TRANS_ID) AS WH_TRANS_NR
      ,T.TRANSPORT_TYPE_NR AS TRANSPORT_TYPE_ID
      ,T.TRANSPORT_TYPE_NR AS TRANSPORT_TYPE_NR
      ,SC_TYPE_OPER.CLASS_NAME AS TRANSPORT_TYPE_NAME
      ,T.MULTI_LU_GROUP_ID
      ,T.APP_NAME AS APP_NAME_VAL
      ,DECODE(T.APP_NAME
             ,'QTR'
             ,QCMP_NLS.GETSTRING('TXT_TRO_BY_RADIO_TERMINAL')
             ,QCMP_NLS.GETSTRING('TXT_TRO_BY_WHITE_PAPERS')) AS APP_NAME
      ,T.IS_AUTO_RDT_REAL
      ,DECODE(T.APP_NAME
             ,'QTR'
             ,SC_IARR_YN.CLASS_NAME
             ,NULL) AS IS_AUTO_RDT_REAL_DESC
      ,T.PRIORITY
      ,PR.CLASS_NAME AS PRIO_DESC
      ,T.CREATION_TYPE
      ,T.DATE_CREATED
      ,T.DATE_ACTIVATED
      ,T.DATE_STARTED
      ,T.DATE_FINISHED
      ,T.USER_CREATED
      ,T.USER_ACTIVATED
      ,T.USER_STARTED
      ,T.USER_FINISHED
      ,SU_PREF.USER_NR AS USER_PREFER_NR
      ,SU_RE.NAME AS USER_REALIZE_NR
      ,TA.NAME AS USER_STRICT_NR
      ,TA.TERMINAL_NR_STRICT
      ,T.TRMEAN_ID
      ,T.TR_GROUP_ID
      ,T.SP_ID_START
      ,T.SP_ID_FINISH
      ,T.LOADUNIT_ID
      ,HLU.LOADUNIT_NR
      ,slu.LOADUNIT_NR AS SUM_LOADUNIT_NR
      ,GL.LOADUNIT_NR AS GROUP_LABEL_NR
      ,R.ROUTE_NR
      ,T.IS_COMPLEX
      ,SC_ICOMPLEX_YN.CLASS_NAME AS IS_COMPLEX_NAME
      ,DECODE(T.OBJECT_ID
             ,-1
             ,NULL
             ,T.OBJECT_ID) AS OBJECT_ID
      ,DECODE(T.OBJECT_NR
             ,'-1'
             ,QCMP_NLS.GETSTRING('TXT_MULTIPLE_OBJECTS')
             ,T.OBJECT_NR) AS OBJECT_NR
      ,SP_FROM.SP_NR AS SP_FROM_NR
      ,SP_TO.SP_NR AS SP_TO_NR
      ,SC_TYPE_OPER.CLASS_NAME AS TRANS_TYPE_NR
      ,TR_GROUPS.TR_GROUP_NR
      ,CASE
          WHEN t.TRANSPORT_TYPE_NR = 'SH' AND t.IS_COMPLEX = 'T' THEN
            (SELECT DECODE(COUNT(DISTINCT pz.PZONE_NR), 0, NULL, 1, MIN(pz.PZONE_NR), 'TXT_MANY') AS PZONE_NR
              FROM   TR_TRANSPORTS_FAST      tr
                    ,TR_TRANSPORT_ITEMS_FAST tri
                    ,QWH_PICK_ZONES_ASSIGN pza
                    ,QWH_PICK_ZONES pz
              WHERE  tr.WH_TRANS_ID = tri.WH_TRANS_ID
              AND    tr.TRANSPORT_TYPE_NR = 'SH'
              AND    pza.SP_ID = tri.LU_SRC_SP_ID
              AND    pz.PZONE_ID = pza.PZONE_ID
              AND    tr.WH_TRANS_ID = t.WH_TRANS_ID)
              WHEN t.TRANSPORT_TYPE_NR in ('MV','RP') AND t.IS_COMPLEX = 'N' THEN
                (SELECT DECODE(COUNT(DISTINCT pz.PZONE_NR), 0, NULL, 1, MIN(pz.PZONE_NR), 'TXT_MANY') AS PZONE_NR
              FROM   TR_TRANSPORTS_FAST      tr
                    ,QWH_PICK_ZONES_ASSIGN pza
                    ,QWH_PICK_ZONES pz
              WHERE  pza.SP_ID = t.sp_id_finish
              AND    pz.PZONE_ID = pza.PZONE_ID
              AND    tr.WH_TRANS_ID = t.WH_TRANS_ID)
              WHEN t.TRANSPORT_TYPE_NR in ('MV','RP') AND t.IS_COMPLEX = 'T' THEN
            (SELECT DECODE(COUNT(DISTINCT pz.PZONE_NR), 0, NULL, 1, MIN(pz.PZONE_NR), 'TXT_MANY') AS PZONE_NR
              FROM   TR_TRANSPORTS_FAST      tr
                    ,TR_TRANSPORT_ITEMS_FAST tri
                    ,QWH_PICK_ZONES_ASSIGN pza
                    ,QWH_PICK_ZONES pz
              WHERE  tr.WH_TRANS_ID = tri.WH_TRANS_ID
              AND    pza.SP_ID = tri.lu_dst_sp_id
              AND    pz.PZONE_ID = pza.PZONE_ID
              AND    tr.WH_TRANS_ID = t.WH_TRANS_ID)
       ELSE
         NULL
       END AS PZONE_NR
      ,WH_FROM.WH_ID AS WH_FROM_ID
      ,WH_FROM.WH_NR AS WH_FROM_NR
      ,WH_TO.WH_NR AS WH_TO_NR
      ,WH_TO.WH_ID AS WH_TO_ID
      ,MN.TRMEAN_NR
      ,T.INFO
      ,T.STATUS
      ,T.DATE_CREATED AS C_DATE
      ,T.USER_CREATED AS C_USER
      ,T.LM_DATE
      ,T.LM_USER
      ,SC.CLASS_NAME AS STATUS_NAME
      ,SC_TYPE_OPER.CLASS_NAME AS OPER_TYPE_NAME
      ,F.FIRM_NR AS F_FIRM_NR
      ,TE.INFO_1
      ,TE.INFO_2
      ,TE.INFO_3
      ,(SELECT string_agg (DISTINCT p.PRODUCT_NR)
          FROM TR_TRANSPORT_PRODUCTS tp, QCM_PRODUCTS p
         WHERE t.WH_TRANS_ID = tp.WH_TRANS_ID
           AND tp.PRODUCT_ID = p.PRODUCT_ID) AS PRODUCT_NR
      ,(null) AS PRODUCT_NAME
      ,T.SORT_DATE AS LOADING_DATE
      ,TRP_SPREAD_TRANSPORT_FAST.ColorSpread(t.app_name) AS CF
      ,(select string_agg(distinct sr.name)
         from qwh_static_routes sr, sor_orders so, sh_ship_items si
        where so.sroute_id = sr.sroute_id
          and si.shipment_id = t.object_id
          and si.order_id = so.order_id
          and so.sroute_id IS NOT NULL) AS SROUTE_NAME
      ,(select string_agg(distinct sr.sroute_nr)
         from qwh_static_routes sr, sor_orders so, sh_ship_items si
        where so.sroute_id = sr.sroute_id
          and si.shipment_id = t.object_id
          and si.order_id = so.order_id
          and so.sroute_id IS NOT NULL) AS SROUTE_NR
FROM   TR_TRANSPORTS_FAST  t
      ,TR_TRANSPORTS_EXT   te
      ,QCM_SYSCLASSES      sc
      ,QCM_SYSCLASSES      sc_iarr_yn
      ,QCM_SYSCLASSES      sc_icomplex_yn
      ,QCM_SYSCLASSES      sc_type_oper
      ,STORAGEPLACES       sp_from
      ,STORAGEAREAS        sa_from
      ,QCM_WAREHOUSES      wh_from
      ,STORAGEPLACES       sp_to
      ,STORAGEAREAS        sa_to
      ,QCM_WAREHOUSES      wh_to
      ,TR_TRANSPORT_GROUPS tr_groups
      ,LOAD_UNITS_FAST     lu
      ,HIST_LOAD_UNITS     hlu
      ,QWH_SUMM_LOADUNITS  slu
      ,QWH_GROUP_LABEL_LOADUNITS GL
      ,QWH_TR_MEANS        mn
      ,QCMV_MODE_ORDERERS  mo
      ,QCM_FIRMS           f
      ,QWH_ROUTES          r
      ,QCM_SYSCLASSES      pr
      ,QCM_SYSUSERS        SU_RE
      ,QCM_SYSUSERS        SU_PREF
      ,(SELECT task.OBJECT_ID
              ,task.TERMINAL_NR_STRICT
              ,w.NAME
       FROM QCM_SYSUSERS w, TMA_TASK_FAST task, TMA_TASK_TYPE tt
       WHERE task.USER_STRICT = w.USER_ID(+) and tt.SERVICE_MODE = 'TR' and tt.TASK_TYPE_ID = task.TASK_TYPE_ID
       ) ta
WHERE  T.STATUS = SC.CLASS_VALUE
AND    T.SP_ID_START = SP_FROM.SP_ID
AND    T.SP_ID_FINISH = SP_TO.SP_ID
AND    T.TR_GROUP_ID = TR_GROUPS.TR_GROUP_ID(+)
AND    TR_GROUPS.ROUTE_ID = R.ROUTE_ID(+)
AND    SP_FROM.SA_ID = SA_FROM.SA_ID
AND    SA_FROM.WH_ID = WH_FROM.WH_ID
AND    (EXISTS
       (SELECT 1
         FROM   QCMV_MODE_WAREHOUSES WH_FROM_MODE
         WHERE  WH_FROM_MODE.WH_ID = WH_FROM.WH_ID) OR EXISTS
       (SELECT 1
         FROM   QCMV_MODE_WAREHOUSES WH_TO_MODE
         WHERE  WH_TO_MODE.WH_ID = WH_TO.WH_ID))
AND    SP_TO.SA_ID = SA_TO.SA_ID
AND    SA_TO.WH_ID = WH_TO.WH_ID
AND    T.LOADUNIT_ID = LU.LOADUNIT_ID
AND    T.LOADUNIT_ID = hlu.LOADUNIT_ID
AND    lu.SUMM_LOADUNIT_ID = slu.LOADUNIT_ID(+)
AND    lu.GROUP_LABEL_ID = GL.LOADUNIT_ID(+)
AND    T.TRMEAN_ID = MN.TRMEAN_ID(+)
AND    SC_IARR_YN.CLASS_TYPE = 'YES_NO'
AND    SC_IARR_YN.CLASS_VALUE = T.IS_AUTO_RDT_REAL
AND    SC_ICOMPLEX_YN.CLASS_TYPE = 'YES_NO'
AND    SC_ICOMPLEX_YN.CLASS_VALUE = T.IS_COMPLEX
AND    SC.CLASS_TYPE = 'WH_TRANSPORTS_STATUS'
AND    T.TRANSPORT_TYPE_NR = SC_TYPE_OPER.CLASS_VALUE(+)
AND    SC_TYPE_OPER.CLASS_TYPE(+) = 'TRANSPORT_OPER_TYPE'
AND    T.STATUS <> '--'
AND    T.WH_TRANS_EXT_ID = TE.WH_TRANS_EXT_ID
AND    LU.OWNER_ID = F.FIRM_ID
AND    LU.OWNER_ID = MO.FIRM_ID(+)
AND    T.USER_STARTED = SU_RE.USER_ID(+)
AND    T.USER_PREFER = SU_PREF.USER_ID(+)
AND    T.WH_TRANS_ID = TA.OBJECT_ID(+)
AND    (MO.FIRM_ID IS NOT NULL OR EXISTS
       (SELECT 1
         FROM   TR_TRANSPORT_ITEMS_FAST TRI
               ,QCM_PRODUCTS       PR2
               ,QCMV_MODE_ORDERERS MO2
         WHERE  pr2.PRODUCT_ID = TRI.PRODUCT_ID
         AND    tri.WH_TRANS_ID = t.WH_TRANS_ID
         AND    pr2.DEFAULT_OWNER_ID = mo2.firm_id
         AND    TRI.STATUS <> '--') AND (T.WH_TRANS_ID IS NOT NULL))
AND    PR.CLASS_TYPE = 'WH_TRANSPORTS_PRIORITY'
AND    nvl(T.PRIORITY,0) = PR.CLASS_VALUE(+)