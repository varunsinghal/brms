<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">

<xsl:variable name="id" select="simple-textbox/id" />

<div class="container">
    <div class="form-group">
        
        <label for="{$id}">
            <xsl:value-of select="simple-textbox/label"/> 
        </label>
        
        <input type="text" class="form-control form-control-sm" id="{$id}">
                <xsl:attribute name="maxlength"> 
                    <xsl:if test="simple-textbox/max-length">
                        <xsl:value-of select="simple-textbox/max-length"/>
                    </xsl:if>
                </xsl:attribute>
        </input>

        <small class="form-text form-text-sm text-muted">
            <xsl:value-of select="simple-textbox/tooltip"/>
        </small>
        
  </div>
</div>

</xsl:template>
</xsl:stylesheet>
