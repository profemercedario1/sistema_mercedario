from fpdf import FPDF
import sqlite3
import os

class PDF(FPDF):
    def header(self):
        # Escudo institucional (si existe)
        try:
            if os.path.exists("escudo_mercedario.png"):
                self.image("escudo_mercedario.png", 10, 8, 20)  # x, y, tamaño
        except Exception as e:
            print("⚠️ No se pudo cargar el escudo:", e)

        # Título de la institución
        self.set_font("Arial", "B", 14)
        self.set_text_color(0, 51, 102)
        self.cell(0, 10, "UNIDAD EDUCATIVA MARIA DE LA MERCED", ln=True, align="C")
        self.ln(5)

        # Línea azul decorativa
        self.set_draw_color(0, 51, 102)
        self.set_line_width(0.6)
        self.line(10, 28, 200, 28)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, "PERIODO LECTIVO 2025 - 2026", 0, 0, "C")

def generar_pdf():
    """Genera un reporte PDF con los estudiantes registrados en la base de datos."""
    try:
        # Conexión a la base de datos
        conn = sqlite3.connect("registros.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM estudiantes")
        registros = cursor.fetchall()
        conn.close()

        if not registros:
            print("⚠️ No hay registros para generar el reporte.")
            return

        pdf = PDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 14)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 10, "REPORTE DE ESTUDIANTES", ln=True, align="C")
        pdf.ln(8)

        # Encabezado de tabla con color
        pdf.set_font("Arial", "B", 10)
        pdf.set_fill_color(0, 51, 102)
        pdf.set_text_color(255, 255, 255)

        headers = ["ID", "NOMBRE", "NOTA 1", "NOTA 2", "NOTA 3", "PROMEDIO"]
        widths = [10, 60, 25, 25, 25, 30]

        for i in range(len(headers)):
            pdf.cell(widths[i], 10, headers[i], 1, 0, "C", fill=True)
        pdf.ln()

        # Cuerpo de la tabla
        pdf.set_font("Arial", "", 10)
        pdf.set_text_color(0, 0, 0)

        for r in registros:
            pdf.cell(10, 10, str(r[0]), 1, 0, "C")
            pdf.cell(60, 10, r[1], 1, 0, "L")
            pdf.cell(25, 10, f"{r[2]:.2f}", 1, 0, "C")
            pdf.cell(25, 10, f"{r[3]:.2f}", 1, 0, "C")
            pdf.cell(25, 10, f"{r[4]:.2f}", 1, 0, "C")
            pdf.cell(30, 10, f"{r[5]:.2f}", 1, 1, "C")

        # Guardar el PDF
        pdf.output("reporte_estudiantes.pdf")
        print("📄 Reporte generado: reporte_estudiantes.pdf")

    except Exception as e:
        print("❌ Error al generar el PDF:", e)
