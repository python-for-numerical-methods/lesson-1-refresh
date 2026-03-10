try:
    from factors import factors
except ImportError:
    print("שגיאה: לא נמצא קובץ בשם solution.py או שהפונקציה get_factors לא הוגדרה.")
    exit(1)
try:
    assert factors(10) == [1, 2, 5, 10], "טעות בגורמים של 10"
    assert factors(13) == [1, 13], "טעות במספר ראשוני (13)"
    assert factors(1) == [1], "טעות במקרה קצה של 1"
    print("כל הכבוד! כל הבדיקות עברו בהצלחה. 🎉")
except AssertionError as e:
    print(f"הבדיקה נכשלה: {e}")
    exit(1) # חשוב להחזיר קוד שגיאה כדי שגיט-האב יסמן 'X'
